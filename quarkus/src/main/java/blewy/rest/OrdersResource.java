package blewy.rest;

import org.apache.pinot.client.Connection;
import org.apache.pinot.client.ConnectionFactory;
import org.apache.pinot.client.Request;    
import org.apache.pinot.client.ResultSet;
import org.apache.pinot.client.ResultSetGroup;
import org.jooq.SQLDialect;
import org.jooq.impl.DSL;

import blewy.models.*;
import blewy.streams.OrdersQueries;

import jakarta.enterprise.context.ApplicationScoped; 
import jakarta.inject.Inject;                       
import jakarta.ws.rs.GET;                          
import jakarta.ws.rs.Path;                         
import jakarta.ws.rs.PathParam;                    
import jakarta.ws.rs.core.Response;     

import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static org.jooq.impl.DSL.*;

@ApplicationScoped
@Path("/orders")
public class OrdersResource {

    @Inject
    OrdersQueries ordersQueries;

    private Connection connection = ConnectionFactory.fromHostList(
            System.getenv().getOrDefault("PINOT_BROKER", "pinot-broker:8099")
    );

    @GET
    @Path("/overview")
    public Response overview() {
        OrdersSummary ordersSummary = ordersQueries.ordersSummary();
        return Response.ok(ordersSummary).build();
    }

    @GET
    @Path("/overview2")
    public Response overview2() {
        runQuery(connection, "select count(*) from orders limit 10");

        String query = DSL.using(SQLDialect.POSTGRES)
                .select(
                        countDistinct(field("order_id"))
                        .filterWhere("time_ms > ago('PT1M')").as("events1Min"),

                        countDistinct(field("order_id"))
                        .filterWhere("time_ms <= ago('PT1M') AND time_ms > ago('PT2M')").as("events1Min2Min"),

                        sumDistinct(field("order_total").coerce(Long.class))
                        .filterWhere("time_ms > ago('PT1M')")
                        .as("total1Min"),

                        sumDistinct(field("order_total").coerce(Long.class))
                        .filterWhere("time_ms <= ago('PT1M') AND time_ms > ago('PT2M')")
                        .as("total1Min2Min"),

                        countDistinct(field("order_id"))
                        .filterWhere("refunded = 'yes' AND time_ms > ago('PT1M')")
                        .as("refunded_events_1min"),

                        countDistinct(field("order_id"))
                        .filterWhere("delivered = 'yes' AND time_ms > ago('PT1M')")
                        .as("deliver_events_1min"),

                        countDistinct(field("order_id"))
                        .filterWhere("fraud_flag = true AND time_ms > ago('PT1M')")
                        .as("fraud_events_1min"),

                        countDistinct(field("order_id"))
                        .filterWhere("refunded = 'yes' AND time_ms <= ago('PT1M') AND time_ms > ago('PT2M')")
                        .as("refunded_events_2min"),

                        countDistinct(field("order_id"))
                        .filterWhere("delivered = 'yes' AND time_ms <= ago('PT1M') AND time_ms > ago('PT2M')")
                        .as("delivered_events_2min"),

                        countDistinct(field("order_id"))
                        .filterWhere("fraud_flag = true AND time_ms <= ago('PT1M') AND time_ms > ago('PT2M')")
                        .as("fraud_events_2min")
                )
                .from("orders")
                .getSQL();

        ResultSet rs = runQuery(connection, query);

        /* -------- current minute -------- */
        long   curOrders    = rs.getLong (0, 0);
        double curRevenue   = rs.getDouble(0, 2);
        double curAOV       = curOrders > 0 ? curRevenue / curOrders : 0.0;
        long   curRefunded  = rs.getLong (0, 4);
        long   curDelivered = rs.getLong (0, 5);
        long   curFraud     = rs.getLong (0, 6);

        TimePeriod currentTimePeriod = new TimePeriod(
                curOrders, curRevenue, curAOV,
                curFraud, curDelivered, curRefunded
        );

        /* -------- previous minute -------- */
        long   prevOrders    = rs.getLong (0, 1);
        double prevRevenue   = rs.getDouble(0, 3);
        double prevAOV       = prevOrders > 0 ? prevRevenue / prevOrders : 0.0;
        long   prevRefunded  = rs.getLong (0, 7);
        long   prevDelivered = rs.getLong (0, 8);
        long   prevFraud     = rs.getLong (0, 9);

        TimePeriod previousTimePeriod = new TimePeriod(
                prevOrders, prevRevenue, prevAOV,
                prevFraud, prevDelivered, prevRefunded
        );

        OrdersSummary ordersSummary = new OrdersSummary(
                currentTimePeriod,
                previousTimePeriod
        );
        return Response.ok(ordersSummary).build();
    }

    @GET
    @Path("/ordersperminute")
    public Response ordersPerMinute() {
        String query = DSL.using(SQLDialect.POSTGRES)
                .select(
                        field("ToDateTime(DATETRUNC('MINUTE', time_ms, 'MILLISECONDS'), 'yyyy-MM-dd HH:mm:ss', 'America/New_York')")
                                .as("dateMin"),

                        countDistinct(field("order_id")).as("orders"),

                        sumDistinct(field("order_total").coerce(Long.class)).as("totalRev"),

                        countDistinct(field("order_id"))
                                .filterWhere("fraud_flag = 'true'")
                                .as("fraudCount"),

                        countDistinct(field("order_id"))
                                .filterWhere("delivered = 'yes'")
                                .as("deliveredCount"),

                        countDistinct(field("order_id"))
                                .filterWhere("refunded = 'yes'")
                                .as("refundedCount")
                )
                .from("orders")
                .where(field("time_ms").greaterThan(field("ago('PT1H')")))
                .groupBy(field("dateMin"))
                .orderBy(field("dateMin").desc())
                .limit(inline(60))
                .getSQL();

        ResultSet rs = runQuery(connection, query);
        int rowCount = rs.getRowCount();
        List<TimeseriesRow> rows = new ArrayList<>();

        for (int i = 0; i < rowCount; i++) {
            String ts        = rs.getString(i, 0);
            long   orders    = rs.getLong  (i, 1);
            double revenue   = rs.getDouble(i, 2);
            long   fraud     = (long) rs.getDouble(i, 3);
            long   delivered = (long) rs.getDouble(i, 4);
            long   refunded  = (long) rs.getDouble(i, 5);

            rows.add(new TimeseriesRow(
                    ts, orders, revenue, fraud, delivered, refunded
            ));
        }

        return Response.ok(rows).build();
    }

    @GET
    @Path("/popular")
    public Response popular() {
        String itemQuery = DSL.using(SQLDialect.POSTGRES)
                .select(
                        field("line_items.product.name").as("itemName"),

                        countDistinct(field("order_id")).as("orders"),

                        field("SUMMV(line_items.quantity)", Double.class).as("quantity")
                )
                .from("orders")
                .where(field("time_ms").greaterThan(field("ago('PT1M')")))
                .groupBy(field("line_items.product.name"))
                .orderBy(field("quantity").desc())
                .limit(inline(5))
                .getSQL();

        ResultSet itemRs = runQuery(connection, itemQuery);
        List<PopularItem> popularItems = new ArrayList<>();

        for (int i = 0; i < itemRs.getRowCount(); i++) {
            long   orders   = itemRs.getLong  (i, 1);
            double quantity = itemRs.getDouble(i, 2);
            popularItems.add(
                    new PopularItem(
                        itemRs.getString(i, 0),
                        orders,
                        quantity
                    )
            );
        }

        String categoryQuery = DSL.using(SQLDialect.POSTGRES)
                .select(
                        field("line_items.product.category").as("category"),

                        countDistinct(field("order_id")).as("orders"),

                        field("SUMMV(line_items.quantity)", Double.class).as("quantity")
                )
                .from("orders")
                .where(field("time_ms").greaterThan(field("ago('PT1M')")))
                .groupBy(field("line_items.product.category"))
                .orderBy(field("quantity").desc())
                .limit(inline(5))
                .getSQL();

        ResultSet catRs = runQuery(connection, categoryQuery);
        List<PopularCategory> popularCategories = new ArrayList<>();

        for (int i = 0; i < catRs.getRowCount(); i++) {
            long   orders   = catRs.getLong  (i, 1);
            double quantity = catRs.getDouble(i, 2);
            popularCategories.add(
                    new PopularCategory(catRs.getString(i, 0),
                                        orders,
                                        quantity)
            );
        }

        Map<String, Object> result = new HashMap<>();
        result.put("itemNames",  popularItems);
        result.put("categories", popularCategories);

        return Response.ok(result).build();
    }

    @GET
    @Path("/latestorders")
    public Response latestOrders() {
        String query = DSL.using(SQLDialect.POSTGRES)
                .select(
                        field("order_id"),

                        field("ToDateTime(MAX(time_ms), 'yyyy-MM-dd HH:mm:ss', 'America/New_York')")
                                .as("time_ny"),

                        field("MAX(order_total)").as("order_total"),

                        field("customer_id"),

                        field("MAX(productsOrdered)").as("productsOrdered"),

                        field("MAX(totalQuantity)").as("totalQuantity")
                )
                .from("orders")
                .groupBy(
                field("order_id"),
                field("customer_id")
                )
                .orderBy(field("time_ny").desc())
                .limit(inline(10))
                .getSQL();

        ResultSet summaryResults = runQuery(connection, query);
        int rowCount = summaryResults.getRowCount();
        List<OrderRow> rows = new ArrayList<>();

        for (int index = 0; index < rowCount; index++) {
            rows.add(new OrderRow(
                    summaryResults.getString(index, 0),
                    summaryResults.getString(index, 1),
                    summaryResults.getDouble(index, 2),
                    summaryResults.getString(index, 3),
                    (long) summaryResults.getDouble(index, 4),
                    (long) summaryResults.getDouble(index, 5)
            ));
        }

        return Response.ok(rows).build();
    }

    @GET
    @Path("/couponslastminute")
    public Response couponsLastMinute() {

        String query = DSL.using(SQLDialect.POSTGRES)
                .select(
                        field("coupon_codes.name").as("coupon_code"),

                        countDistinct(field("order_id")).as("orders")
                )
                .from("orders")
                .where(field("coupon_codes.name").isNotNull().and("time_ms > ago('PT1M')"))
                .groupBy(field("coupon_codes.name"))
                .orderBy(field("orders").desc())
                .getSQL();

        ResultSet rs = runQuery(connection, query);
        List<Map<String, Object>> rows = new ArrayList<>();

        for (int i = 0; i < rs.getRowCount(); i++) {
            rows.add(Map.of(
                    "coupon_code", rs.getString(i, 0),
                    "times_used",  rs.getLong  (i, 1)
            ));
        }
        return Response.ok(rows).build();
    }

    @GET
    @Path("/toplocations")
    public Response topLocations() {

        String cityQuery = DSL.using(SQLDialect.POSTGRES)
            .select(
                field("shipping_address_city").as("city"),

                countDistinct(field("order_id")).as("totalOrders")
            )
            .from("orders")
            .where(field("time_ms").greaterThan(field("ago('PT1M')")))
            .groupBy(field("shipping_address_city"))
            .orderBy(field("totalOrders").desc())
            .limit(inline(5))
            .getSQL();

        ResultSet cityRs = runQuery(connection, cityQuery);
        List<Map<String, Object>> topCities = new ArrayList<>();

        for (int i = 0; i < cityRs.getRowCount(); i++) {
            topCities.add(Map.of(
                "city",        cityRs.getString(i, 0),
                "totalOrders", cityRs.getLong  (i, 1)
            ));
        }

        String stateQuery = DSL.using(SQLDialect.POSTGRES)
            .select(
                field("shipping_address_state").as("state"),

                countDistinct(field("order_id")).as("totalOrders")
            )
            .from("orders")
            .where(field("time_ms").greaterThan(field("ago('PT1M')")))
            .groupBy(field("shipping_address_state"))
            .orderBy(field("totalOrders").desc())
            .limit(inline(5))
            .getSQL();

        ResultSet stateRs = runQuery(connection, stateQuery);
        List<Map<String, Object>> topStates = new ArrayList<>();

        for (int i = 0; i < stateRs.getRowCount(); i++) {
            topStates.add(Map.of(
                "state",       stateRs.getString(i, 0),
                "totalOrders", stateRs.getLong  (i, 1)
            ));
        }

        Map<String, Object> result = new HashMap<>();
        result.put("cities", topCities);
        result.put("states", topStates);

        return Response.ok(result).build();
    }

    /** Single‑stage Pinot Query*/
    private static ResultSet runQuery(Connection conn, String sql) {
        return conn.execute(sql).getResultSet(0);
    }

    /** Multi‑stage Pinot Query */
    private static ResultSet runQueryMS(Connection conn, String sql) {
        String multiStageSql = "SET useMultistageEngine=true; " + sql;
        return conn.execute(multiStageSql).getResultSet(0);
    }
}    