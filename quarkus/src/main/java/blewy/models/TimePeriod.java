package blewy.models;

import io.quarkus.runtime.annotations.RegisterForReflection;

@RegisterForReflection
public class TimePeriod {

    private long   orders;
    private double totalRevenue;
    private double avgOrderValue;
    private long   fraudCount;
    private long   deliveredCount;
    private long   refundedCount;

    public TimePeriod(long orders,
                      double totalRevenue,
                      double avgOrderValue,
                      long fraudCount,
                      long deliveredCount,
                      long refundedCount) {
        this.orders         = orders;
        this.totalRevenue     = totalRevenue;
        this.avgOrderValue  = avgOrderValue;
        this.fraudCount     = fraudCount;
        this.deliveredCount = deliveredCount;
        this.refundedCount  = refundedCount;
    }

    public TimePeriod() {}

    public TimePeriod(long orders, double totalRevenue) {
        this.orders        = orders;
        this.totalRevenue    = totalRevenue;
        this.avgOrderValue = orders > 0 ? totalRevenue / orders : 0.0;
    }


    public void addOrder(CompleteOrder order) {
        orders++;
        totalRevenue    += order.order_total;
        avgOrderValue  = orders > 0 ? totalRevenue / orders : 0.0;

        if ("true".equalsIgnoreCase(order.fraud_flag))  fraudCount++;
        if ("yes".equalsIgnoreCase(order.delivered))    deliveredCount++;
        if ("yes".equalsIgnoreCase(order.refunded))     refundedCount++;
    }


    public long   getOrders()         { return orders;        }
    public double getTotalRevenue()     { return totalRevenue;    }
    public double getAvgOrderValue()  { return avgOrderValue; }
    public long   getFraudCount()     { return fraudCount;    }
    public long   getDeliveredCount() { return deliveredCount;}
    public long   getRefundedCount()  { return refundedCount; }
}
