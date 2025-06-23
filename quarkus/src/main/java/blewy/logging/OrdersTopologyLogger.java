package blewy.logging;

import blewy.models.Order;
import blewy.models.OrderItem;
import org.apache.kafka.streams.kstream.Windowed;
import org.jboss.logging.Logger;

import java.time.Instant;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;
import java.util.List;

public final class OrdersTopologyLogger {

    private static final Logger LOG = Logger.getLogger(OrdersTopologyLogger.class);
    private static final DateTimeFormatter TS = DateTimeFormatter.ISO_INSTANT;

    private OrdersTopologyLogger() {
    }

    public static void rawRecord(String key, String value) {
        if (LOG.isTraceEnabled()) {
            LOG.tracef("RAW  key=%s  payload=%s", key, value);
        }
    }

    public static void parsedOrder(String key, Order order) {
        if (LOG.isDebugEnabled()) {
            if (order == null) {
                LOG.debugf("PARSE-FAIL key=%s  (order == null)", key);
            } else {
                LOG.debugf("PARSED key=%s  orderId=%s  total=%.2f  ts=%s",
                           key,
                           order.order_id,
                           order.order_total,
                           order.timestamp);
            }
        }
    }

    public static void fraudFlagged(Order order) {
        if (LOG.isInfoEnabled() && order != null) {
            LOG.infof("FRAUD  orderId=%s  customer=%s  total=%.2f  ts=%s",
                      order.order_id,
                      customerId(order),
                      order.order_total,
                      order.timestamp);
        }
    }

    public static void delivered(Order order) {
        if (LOG.isDebugEnabled() && order != null) {
            LOG.debugf("DELIVERED orderId=%s  customer=%s  ts=%s",
                       order.order_id,
                       customerId(order),
                       order.timestamp);
        }
    }

    public static void refunded(Order order) {
        if (LOG.isEnabled(Logger.Level.WARN) && order != null) {
            LOG.warnf("REFUND orderId=%s  customer=%s  amount=%.2f  ts=%s",
                      order.order_id,
                      customerId(order),
                      order.order_total,
                      order.timestamp);
        }
    }

    public static void windowCount(String metricName,
                                   Windowed<String> window,
                                   long count) {

        if (LOG.isInfoEnabled()) {
            LOG.infof("AGG-COUNT metric=%s  key=%s  win=[%s,%s)  count=%d",
                      metricName,
                      window.key(),
                      window.window().start(),
                      window.window().end(),
                      count);
        }
    }

    public static void windowAggregate(String metricName,
                                       Windowed<String> window,
                                       double value) {

        if (LOG.isInfoEnabled()) {
            LOG.infof("AGG-VALUE metric=%s  key=%s  win=[%s,%s)  value=%.2f",
                      metricName,
                      window.key(),
                      window.window().start(),
                      window.window().end(),
                      value);
        }
    }

    private static String customerId(Order o) {
        return (o != null && o.customer != null) ? o.customer.customer_id : "unknown";
    }

    public static void orderItems(String orderId, List<OrderItem> items) {
        if (LOG.isTraceEnabled() && items != null) {
            for (OrderItem it : items) {
                if (it != null && it.product != null) {
                    double itemTotal = it.quantity * it.product.price;
                    LOG.tracef("ITEM orderId=%s  product=%s  qty=%d  price=%.2f",
                               orderId,
                               it.product.product_id,
                               it.quantity,
                               itemTotal);
                }
            }
        }
    }
}
