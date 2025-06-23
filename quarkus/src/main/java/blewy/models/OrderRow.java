package blewy.models;

import io.quarkus.runtime.annotations.RegisterForReflection;

@RegisterForReflection
public class OrderRow {

    private final String orderId;
    private final String timestamp;
    private final double orderTotal;
    private final String customerId;
    private final long productsOrdered;
    private final long totalQuantity;

    public OrderRow(String orderId, String timestamp, double orderTotal, String customerId, long productsOrdered, long totalQuantity) {
        this.orderId = orderId;
        this.timestamp = timestamp;        
        this.orderTotal = orderTotal;
        this.customerId = customerId;
        this.productsOrdered = productsOrdered;
        this.totalQuantity = totalQuantity;
    }

    public String orderId() {
        return orderId;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public double getOrderTotal() {
        return orderTotal;
    }

    public String getCustomerId() {
        return customerId;
    }

    public long getProductsOrdered() {
        return productsOrdered;
    }

    public long getTotalQuantity() {
        return totalQuantity;
    }
}
