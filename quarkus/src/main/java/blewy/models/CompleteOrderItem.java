package blewy.models;

public class CompleteOrderItem {
    public Product product;
    public int quantity;
    public int free_qty;

    public CompleteOrderItem() {
    }

    public CompleteOrderItem(Product product, int quantity, int free_qty) {
        this.product = product;
        this.quantity = quantity;
        this.free_qty = free_qty;
    }
}
