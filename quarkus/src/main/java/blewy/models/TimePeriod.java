package blewy.models;

import io.quarkus.runtime.annotations.RegisterForReflection;

@RegisterForReflection
public class TimePeriod {

    private long   orders;
    private double totalPrice;
    private double avgOrderValue;
    private long   fraudCount;
    private long   deliveredCount;
    private long   refundedCount;

    public TimePeriod(long orders,
                      double totalPrice,
                      double avgOrderValue,
                      long fraudCount,
                      long deliveredCount,
                      long refundedCount) {
        this.orders         = orders;
        this.totalPrice     = totalPrice;
        this.avgOrderValue  = avgOrderValue;
        this.fraudCount     = fraudCount;
        this.deliveredCount = deliveredCount;
        this.refundedCount  = refundedCount;
    }

    public TimePeriod() {}

    public TimePeriod(long orders, double totalPrice) {
        this.orders        = orders;
        this.totalPrice    = totalPrice;
        this.avgOrderValue = orders > 0 ? totalPrice / orders : 0.0;
    }


    public void addOrder(CompleteOrder order) {
        orders++;
        totalPrice    += order.order_total;
        avgOrderValue  = orders > 0 ? totalPrice / orders : 0.0;

        if ("true".equalsIgnoreCase(order.fraud_flag))  fraudCount++;
        if ("yes".equalsIgnoreCase(order.delivered))    deliveredCount++;
        if ("yes".equalsIgnoreCase(order.refunded))     refundedCount++;
    }


    public long   getOrders()         { return orders;        }
    public double getTotalPrice()     { return totalPrice;    }
    public double getAvgOrderValue()  { return avgOrderValue; }
    public long   getFraudCount()     { return fraudCount;    }
    public long   getDeliveredCount() { return deliveredCount;}
    public long   getRefundedCount()  { return refundedCount; }
}
