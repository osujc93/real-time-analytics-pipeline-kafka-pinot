package blewy.rest;

import org.apache.pinot.client.Connection;
import org.apache.pinot.client.ConnectionFactory;
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
                        field("ToDateTime(DATETRUNC('MINUTE', time_ms, 'MILLISECONDS'), 'yyyy-MM-dd HH:mm:ss', 'America/New_York')").as("dateMin"),
                        // total unique orders per minute
                        countDistinct(field("order_id")).as("orders"),

                        // deduped revenue per minute
                        sumDistinct(field("order_total").coerce(Long.class)).as("totalRev"),

                        // unique orders that are fraud / delivered / refunded
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
                .orderBy(field("dateMin"))
                .limit(inline(60))
                .getSQL();

        ResultSet rs = runQuery(connection, query);
        int rowCount = rs.getRowCount();
        List<TimeseriesRow> rows = new ArrayList<>();

        for (int i = 0; i < rowCount; i++) {
            String ts        = rs.getString(i, 0);
            long   orders    = rs.getLong  (i, 1);               // safe – COUNT DISTINCT
            double revenue   = rs.getDouble(i, 2);               // totalRev
            long   fraud     = (long) rs.getDouble(i, 3);        // fraudCount
            long   delivered = (long) rs.getDouble(i, 4);        // deliveredCount
            long   refunded  = (long) rs.getDouble(i, 5);        // refundedCount

            rows.add(new TimeseriesRow(
                    ts, orders, revenue, fraud, delivered, refunded
            ));
        }

        return Response.ok(rows).build();
    }

    @GET
    @Path("/popular")
    public Response popular() {
        /* ---------- top 5 items ---------- */
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

        /* ---------- top 5 categories ---------- */
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
                        field("ToDateTime(MAX(time_ms), 'yyyy-MM-dd HH:mm:ss', 'America/New_York')").as("time_ny"),
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
                    summaryResults.getString(index, 0),                 // order_id
                    summaryResults.getString(index, 1),                 // timestamp (formatted)
                    summaryResults.getDouble(index, 2),                 // order_total
                    summaryResults.getString(index, 3),                 // customer_id
                    (long) summaryResults.getDouble(index, 4),          // productsOrdered
                    (long) summaryResults.getDouble(index, 5)           // totalQuantity
            ));
        }

        return Response.ok(rows).build();
    }

    private static ResultSet runQuery(Connection connection, String query) {
        ResultSetGroup resultSetGroup = connection.execute(query);
        return resultSetGroup.getResultSet(0);
    }
}
