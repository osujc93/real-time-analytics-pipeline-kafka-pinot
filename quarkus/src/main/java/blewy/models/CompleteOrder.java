package blewy.models;

import java.util.ArrayList;
import java.util.List;

public class CompleteOrder {

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

    public List<String> coupon_codes;
    public Object status_history;
    public Object billing_address;
    public Object shipping_address;
    public Object customer;
    public List<CompleteOrderItem> line_items;
    public List<Object> shipments;
    public String pet_name;
    public String subscription_id;
    public String subscription_frequency;
    public String payment_info;
    public String fraud_flag;

    public String tracking_number;

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

    public long timestamp;
    public long time_ms;

    public CompleteOrder() {
        this.coupon_codes = new ArrayList<>();
        this.line_items = new ArrayList<>();
        this.shipments = new ArrayList<>();
    }
}
