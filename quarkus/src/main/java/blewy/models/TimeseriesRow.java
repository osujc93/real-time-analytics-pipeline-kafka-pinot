package blewy.models;

import io.quarkus.runtime.annotations.RegisterForReflection;

@RegisterForReflection
public class TimeseriesRow {
    private final String timestamp;
    private final long orders;
    private final double revenue;
    private final long fraud;
    private final long delivered;
    private final long refunded;

    public TimeseriesRow(String timestamp, long orders, double revenue,
                         long fraud, long delivered, long refunded) {
        this.timestamp = timestamp;
        this.orders = orders;
        this.revenue = revenue;
        this.fraud = fraud;
        this.delivered = delivered;
        this.refunded = refunded;
    }

    public String getTimestamp() {
        return timestamp;
    }
    public long getOrders() {
        return orders;
    }
    public double getRevenue() {
        return revenue;
    }
    public long getFraud() {
        return fraud;
    }
    public long getDelivered() {
        return delivered;
    }
    public long getRefunded() {
        return refunded;
    }
}
