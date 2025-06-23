package blewy.streams;

import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StoreQueryParameters;
import org.apache.kafka.streams.errors.InvalidStateStoreException;
import org.apache.kafka.streams.state.*;
import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.kstream.Windowed;

import blewy.models.*;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;

import java.time.Instant;
import java.util.List;
import java.util.Spliterator;
import java.util.Spliterators;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

@ApplicationScoped
public class OrdersQueries {

    @Inject
    KafkaStreams streams;

    public OrdersSummary ordersSummary() {
        KStreamsWindowStore<Long>   countStore     = new KStreamsWindowStore<>(ordersCountsStore(),   "count");
        KStreamsWindowStore<Double> revenueStore   = new KStreamsWindowStore<>(revenueStore(),        "count");
        KStreamsWindowStore<Long>   fraudStore     = new KStreamsWindowStore<>(fraudCountStore(),     "fraud");
        KStreamsWindowStore<Long>   deliveredStore = new KStreamsWindowStore<>(deliveredCountStore(), "count");
        KStreamsWindowStore<Long>   refundedStore  = new KStreamsWindowStore<>(refundedCountStore(),  "count");

        Instant  now           = Instant.now();
        Instant  oneMinuteAgo  = now.minusSeconds(60);
        Instant  twoMinutesAgo = now.minusSeconds(120);

        long   recentCount     = countStore.firstEntry(oneMinuteAgo, now);
        double recentRevenue   = revenueStore.firstEntry(oneMinuteAgo, now);
        long   recentFraud     = fraudStore.firstEntry(oneMinuteAgo, now);
        long   recentDelivered = deliveredStore.firstEntry(oneMinuteAgo, now);
        long   recentRefunded  = refundedStore.firstEntry(oneMinuteAgo, now);
        double recentAOV       = recentCount > 0 ? recentRevenue / recentCount : 0.0;

        long   prevCount       = countStore.firstEntry(twoMinutesAgo, oneMinuteAgo);
        double prevRevenue     = revenueStore.firstEntry(twoMinutesAgo, oneMinuteAgo);
        long   prevFraud       = fraudStore.firstEntry(twoMinutesAgo, oneMinuteAgo);
        long   prevDelivered   = deliveredStore.firstEntry(twoMinutesAgo, oneMinuteAgo);
        long   prevRefunded    = refundedStore.firstEntry(twoMinutesAgo, oneMinuteAgo);
        double prevAOV         = prevCount > 0 ? prevRevenue / prevCount : 0.0;

        TimePeriod current  = new TimePeriod(recentCount, recentRevenue, recentAOV,
                                             recentFraud, recentDelivered, recentRefunded);
        TimePeriod previous = new TimePeriod(prevCount,   prevRevenue,   prevAOV,
                                             prevFraud,   prevDelivered, prevRefunded);

        return new OrdersSummary(current, previous);
    }

    private ReadOnlyWindowStore<String, Double>   revenueStore()        { return fetchWindowStore("RevenueStore"); }
    private ReadOnlyWindowStore<String, Long>     ordersCountsStore()   { return fetchWindowStore("OrdersCountStore"); }
    private ReadOnlyWindowStore<String, Long>     fraudCountStore()     { return fetchWindowStore("FraudCountStore"); }
    private ReadOnlyWindowStore<String, Long>     deliveredCountStore() { return fetchWindowStore("DeliveredCountStore"); }
    private ReadOnlyWindowStore<String, Long>     refundedCountStore()  { return fetchWindowStore("RefundedCountStore"); }

    private <V> ReadOnlyWindowStore<String, V> fetchWindowStore(String storeName) {
        while (true) {
            try {
                return streams.store(StoreQueryParameters.fromNameAndType(storeName,
                                                                          QueryableStoreTypes.windowStore()));
            } catch (InvalidStateStoreException e) {
            }
        }
    }

    private static <K, V> Stream<KeyValue<K, V>> toStream(KeyValueIterator<K, V> iterator) {
        return StreamSupport.stream(
                Spliterators.spliteratorUnknownSize(iterator, Spliterator.ORDERED),
                false
        );
    }
}
