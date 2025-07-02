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
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static org.jooq.impl.DSL.*;

@ApplicationScoped
@Path("/users")
public class UsersResource {
    private Connection connection = ConnectionFactory.fromHostList(
            System.getenv().getOrDefault("PINOT_BROKER",  "pinot-broker:8099")
    );

    @GET
    @Path("/{customerId}/orders")
    public Response userOrders(@PathParam("customerId") String customerId) {

        String query = DSL.using(SQLDialect.POSTGRES)
                .select(
                    field("order_id"),

                    field("order_total"),

                    field("ToDateTime(MAX(time_ms), 'yyyy-MM-dd HH:mm:ss', 'America/New_York')")
                            .as("time_ny")
                )
                .from("orders")
                .where(field("customer_id").eq(field("'" + customerId + "'")))
                .groupBy(field("order_id"))
                .orderBy(field("time_ny").desc())
                .limit(DSL.inline(50))
                .getSQL();

        ResultSet resultSet = runQuery(connection, query);
        List<Map<String, Object>> rows = new ArrayList<>();

        for (int index = 0; index < resultSet.getRowCount(); index++) {
            rows.add(Map.of(
                    "order_id", resultSet.getString(index, 0),
                    "order_total", resultSet.getDouble(index, 1),
                    "timestamp", resultSet.getString(index, 2)
            ));
        }

        return Response.ok(rows).build();
    }

    @GET
    @Path("/")
    public Response allUsers() {

        String query = DSL.using(SQLDialect.POSTGRES)
                .select(
                        field("customer_id"),

                        field("ToDateTime(MAX(time_ms), 'yyyy-MM-dd HH:mm:ss', 'America/New_York')")
                                .as("time_ny")
                )
                .from("orders")
                .groupBy(field("customer_id"))
                .orderBy(field("time_ny").desc())
                .limit(DSL.inline(50))
                .getSQL();

        ResultSet resultSet = runQuery(connection, query);

        Stream<Map<String, Object>> rows = IntStream.range(0, resultSet.getRowCount())
                .mapToObj(index -> Map.of(
                    "customer_id", resultSet.getString(index, 0),
                    "timestamp", resultSet.getString  (index, 1)
                ));

        return Response.ok(rows).build();
    }

    private static ResultSet runQuery(Connection connection, String query) {
        ResultSetGroup resultSetGroup = connection.execute(query);
        return resultSetGroup.getResultSet(0);
    }
}
