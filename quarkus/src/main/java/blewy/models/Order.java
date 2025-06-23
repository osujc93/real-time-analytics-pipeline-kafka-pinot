package blewy.models;

import io.quarkus.runtime.annotations.RegisterForReflection;
import com.fasterxml.jackson.databind.JsonNode;

import java.util.List;

@RegisterForReflection
public class Order {

    // Dimension-like fields
    public String order_id;
    public String currency;
    public String payment_method;
    public String delivered;
    public String delivery_date;
    public String refunded;
    public String shipping_provider;
    public String shipping_speed;
    public String shipping_status;
    public String loyalty_tier;
    public String payment_status;
    public String expected_delivery_date;
    public String fulfillment_center;

    // Multi-value dimension
    public List<String> coupon_codes;

    // JSON fields
    public JsonNode status_history;      
    public JsonNode billing_address;     
    public JsonNode shipping_address;    
    public JsonNode shipments;          

    // Nested typed object for convenience
    public Customer customer;

    // line_items array
    public List<OrderItem> line_items;

    public String pet_name;
    public String subscription_id;
    public String subscription_frequency;
    public String payment_info;
    public String fraud_flag;

    // Metric fields
    public double order_total;
    public int risk_score;
    public double exchange_rate;
    public double env_fee;
    public double shipping_cost;
    public double partial_refund_amount;
    public double subtotal_after_coupon;
    public double subtotal_before_promos;
    public double tax_amount;
    public double tax_rate;
    public int loyalty_points_used;
    public int productsOrdered;
    public int totalQuantity;

    public String timestamp;
    public long time_ms;

    public String tracking_number;

    public Order() {
    }

    @RegisterForReflection
    public static class Customer {
        public String customer_id;
        public String address;
        public String city;
        public String email;
        public String name;
        public String phone;
        public String state;
        public String zipcode;

        public Customer() {
        }
    }
}
