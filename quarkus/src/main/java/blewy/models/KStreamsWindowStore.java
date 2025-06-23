package blewy.models;

import org.apache.kafka.streams.state.ReadOnlyWindowStore;
import org.apache.kafka.streams.state.WindowStoreIterator;

import java.time.Instant;


public class KStreamsWindowStore<T> {

    private final ReadOnlyWindowStore<String, T> store;
    private final String key;


    public KStreamsWindowStore(ReadOnlyWindowStore<String, T> store,
                               String key) {
        this.store = store;
        this.key   = key;
    }


    public KStreamsWindowStore(ReadOnlyWindowStore<String, T> store) {
        this(store, "count");
    }


    public T firstEntry(Instant from, Instant to) {
        try (WindowStoreIterator<T> iterator = store.fetch(key, from, to)) {
            if (iterator.hasNext()) {
                return iterator.next().value;
            }
        }
        throw new RuntimeException(
            "No entries found in store for key '" + key +
            "' between " + from + " and " + to
        );
    }
}
