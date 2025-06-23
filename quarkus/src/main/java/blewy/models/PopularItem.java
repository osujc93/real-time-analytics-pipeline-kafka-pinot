package blewy.models;

import io.quarkus.runtime.annotations.RegisterForReflection;

@RegisterForReflection
public class PopularItem {

    private final String itemName;
    private final long   orders;
    private final double quantity;

    public PopularItem() {
        this(null, 0L, 0.0);
    }

    public PopularItem(String itemName, long orders, double quantity) {
        this.itemName = itemName;
        this.orders   = orders;
        this.quantity = quantity;
    }

    public String getItemName() {
        return itemName;
    }

    public long getOrders() {
        return orders;
    }

    public double getQuantity() {
        return quantity;
    }
}
