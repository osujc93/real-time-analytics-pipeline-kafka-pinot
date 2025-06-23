package blewy.streams;

import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.utils.Bytes;
import org.apache.kafka.streams.*;
import org.apache.kafka.streams.kstream.*;
import org.apache.kafka.streams.state.WindowStore;

import blewy.deser.JsonDeserializer;
import blewy.deser.JsonSerializer;
import blewy.models.*;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.enterprise.inject.Produces;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;

@ApplicationScoped
public class OrdersTopology {

    @Produces
    public Topology buildTopology() {

        final Serde<Order>    orderSerde  = Serdes.serdeFrom(new JsonSerializer<>(), new JsonDeserializer<>(Order.class));
        final Serde<String>   stringSerde = Serdes.String();
        final Serde<Integer>  intSerde    = Serdes.Integer();

        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, Order> orders =
                builder.stream("FakeEcommOrders", Consumed.with(Serdes.String(), orderSerde));

        TimeWindows timeWindow = TimeWindows
                .ofSizeAndGrace(Duration.ofSeconds(60), Duration.ofMinutes(5))
                .advanceBy(Duration.ofSeconds(1));

        orders.groupBy((k, v) -> "count", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .count(Materialized.as("OrdersCountStore"));

        orders.groupBy((k, v) -> "count", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .aggregate(() -> 0.0,
                         (k, v, agg) -> agg + v.order_total,
                         Materialized.<String, Double, WindowStore<Bytes, byte[]>>as("RevenueStore")
                                     .withValueSerde(Serdes.Double()));

        orders.filter((k, v) -> v != null && isFraud(v))
              .groupBy((k, v) -> "fraud", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .count(Materialized.as("FraudCountStore"));

        orders.filter((k, v) -> v != null && "yes".equalsIgnoreCase(v.delivered))
              .groupBy((k, v) -> "count", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .count(Materialized.as("DeliveredCountStore"));

        orders.filter((k, v) -> v != null && "yes".equalsIgnoreCase(v.refunded))
              .groupBy((k, v) -> "count", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .count(Materialized.as("RefundedCountStore"));

        return builder.build();
    }

    private static boolean isFraud(Order o) {
        try {
            try { return (Boolean) o.getClass().getMethod("isFraud_flag").invoke(o); }
            catch (NoSuchMethodException ignore) {}

            Object raw = o.getClass().getField("fraud_flag").get(o);
            if (raw instanceof Boolean b) return b;
            if (raw instanceof String  s) return Boolean.parseBoolean(s);

        } catch (Exception ignore) { }
        return false;
    }
}
