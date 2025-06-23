package blewy.models;

/**
 * Represents the objects inside "line_items" array for the "orders" schema.
 * We add "free_qty" since it appears in the Kafka JSON for line_items.
 */
public class CompleteOrderItem {
    public Product product;
    public int quantity;
    public int free_qty; // present in the line_items JSON

    public CompleteOrderItem() {
    }

    public CompleteOrderItem(Product product, int quantity, int free_qty) {
        this.product = product;
        this.quantity = quantity;
        this.free_qty = free_qty;
    }
}
