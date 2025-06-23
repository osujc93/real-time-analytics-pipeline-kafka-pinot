package blewy.models;

import io.quarkus.runtime.annotations.RegisterForReflection;

/**
 * Represents a single line item in the 'line_items' JSON array.
 */
@RegisterForReflection
public class OrderItem {

    public int free_qty;       // e.g., "free_qty": 0
    public int quantity;       // e.g., "quantity": 2
    public Product product;    // e.g., "product": { ... }

    public OrderItem() {
    }

    @RegisterForReflection
    public static class Product {
        public String category;       // e.g., "category": "Purina Veterinary Diet (Dog)"
        public String name;           // e.g., "name": "Purina Pro Plan Vet Diet EN Gastroenteric (Dog) - Canned 12.5OZ CASE24"
        public boolean out_of_stock;  // e.g., "out_of_stock": false
        public double price;          // e.g., "price": 74.99
        public String product_id;     // e.g., "product_id": "124f8142-8fa4-4b18-bb02-da9771c5d8f7"
        public int stock;            // e.g., "stock": 29

        public Product() {
        }
    }
}
