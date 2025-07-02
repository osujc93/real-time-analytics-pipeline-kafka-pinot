package blewy.models;

import io.quarkus.runtime.annotations.RegisterForReflection;

@RegisterForReflection
public class OrderItem {

    public int free_qty;
    public int quantity;
    public Product product;

    public OrderItem() {
    }

    @RegisterForReflection
    public static class Product {
        public String category;
        public String name;
        public boolean out_of_stock;
        public double price;
        public String product_id;
        public int stock;

        public Product() {
        }
    }
}
