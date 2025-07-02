import uuid
from datetime import datetime
from typing import List

from address import Address
from customer import Customer
from order_item import OrderItem
from order_status_history import OrderStatusHistory
from shipment_record import ShipmentRecord
from promotions import (
    B2G1_PROMOS,
    COUPON_DETAILS,
    COUPON_USAGE,
)

class Order:
    @staticmethod
    def _normalise_coupon_codes(raw):

        if not raw:
            return []
        codes = []
        for item in raw:
            if isinstance(item, dict):
                codes.append(item.get("name") or next(iter(item.values()), None))
            else:
                codes.append(item)
        return [c for c in codes if c]

    def __init__(
            self,
            customer,
            line_items,
            payment_info,
            pet_name,
            shipping_address=None,
            billing_address=None,
            coupon_codes=None,
            shipping_speed=None,
            shipping_cost=0.0,
            fulfillment_center=None,
            timestamp=None,
            shipping_status=None,
            expected_delivery_date=None,
            delivery_date=None,
            refunded="no",
            delivered="no",
            payment_status="authorized",
            payment_method="credit_card",
            partial_refund_amount=0.0,
            tax_rate=0.0,
            tax_amount=0.0,
            env_fee=0.0,
            currency="USD",
            exchange_rate=1.0,
            loyalty_points_used=0,
            loyalty_tier="None",
            risk_score=0,
            fraud_flag=False,
            subscription_id=None,
            subscription_frequency=None
    ):
        self.order_id = str(uuid.uuid4())
        self.customer = customer
        self.line_items = line_items
        self.payment_info = payment_info
        self.pet_name = pet_name

        self.shipping_address = shipping_address
        self.billing_address = billing_address

        self.timestamp = (
            timestamp
            or datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        )
        self.shipping_status = shipping_status or "Pending"
        self.expected_delivery_date = expected_delivery_date
        self.delivery_date = delivery_date
        self.refunded = refunded
        self.delivered = delivered

        self.payment_status = payment_status
        self.payment_method = payment_method
        self.partial_refund_amount = partial_refund_amount

        if coupon_codes is None:
            coupon_codes = []
        self.coupon_codes = coupon_codes

        self.shipping_speed = shipping_speed
        self.shipping_cost = shipping_cost
        self.fulfillment_center = fulfillment_center

        self.tax_rate = tax_rate
        self.tax_amount = tax_amount
        self.env_fee = env_fee

        self.currency = currency
        self.exchange_rate = exchange_rate

        self.loyalty_points_used = loyalty_points_used
        self.loyalty_tier = loyalty_tier
        self.risk_score = risk_score
        self.fraud_flag = fraud_flag

        self.subscription_id = subscription_id
        self.subscription_frequency = subscription_frequency

        self.shipments = []

        self.status_history = [
            OrderStatusHistory(self.shipping_status).to_dict()
        ]

        self.tracking_number = None
        self.shipping_provider = None

        self.subtotal_before_promos = 0.0
        for item in self.line_items:
            self.subtotal_before_promos += (item.product.price * item.quantity)

        self.apply_b2g1_promos()

        self.subtotal_after_coupon = self.apply_coupons()

        if "FREESHIP" in self.coupon_codes:
            self.shipping_cost = 0.0

        self.order_total = round(
            self.subtotal_after_coupon + self.shipping_cost + self.env_fee + self.tax_amount,
            2
        )

    def apply_b2g1_promos(self):

        for item in self.line_items:
            sku_match = None
            for promo_sku, (buy_x, get_y) in B2G1_PROMOS.items():
                if promo_sku in item.product.name.replace(" ", "_").upper():
                    sku_match = (buy_x, get_y)
                    break
            if sku_match:
                buy_x, get_y = sku_match
                free_qty = (item.quantity // buy_x) * get_y
                item.free_qty = free_qty

    def apply_coupons(self):

        current_subtotal = self.subtotal_before_promos

        for ccode in self.coupon_codes:
            cinfo = COUPON_DETAILS.get(ccode)
            if not cinfo:
                continue
            if COUPON_USAGE[ccode] >= cinfo["usage_limit"]:
                continue

            disc_rate = cinfo["discount"]
            discount_amt = disc_rate * current_subtotal
            current_subtotal -= discount_amt
            COUPON_USAGE[ccode] += 1

            if not cinfo["stackable"]:
                break

        return round(current_subtotal, 2)

    def to_dict(self):
        line_items_list = [item.to_dict() for item in self.line_items]
        return {
            "order_id": self.order_id,
            "customer": self.customer.to_dict(),
            "line_items": line_items_list,
            "subtotal_before_promos": round(self.subtotal_before_promos, 2),
            "subtotal_after_coupon": self.subtotal_after_coupon,
            "shipping_cost": self.shipping_cost,
            "env_fee": self.env_fee,
            "tax_rate": self.tax_rate,
            "tax_amount": self.tax_amount,
            "order_total": self.order_total,
            "payment_info": self.payment_info,
            "pet_name": self.pet_name,
            "timestamp": self.timestamp,
            "shipping_status": self.shipping_status,
            "expected_delivery_date": self.expected_delivery_date,
            "delivery_date": self.delivery_date,
            "refunded": self.refunded,
            "delivered": self.delivered,
            "payment_status": self.payment_status,
            "payment_method": self.payment_method,
            "partial_refund_amount": self.partial_refund_amount,
            "coupon_codes": [{"name": code} for code in self.coupon_codes],
            "fulfillment_center": self.fulfillment_center,
            "shipping_speed": self.shipping_speed,
            "currency": self.currency,
            "exchange_rate": self.exchange_rate,
            "loyalty_points_used": self.loyalty_points_used,
            "loyalty_tier": self.loyalty_tier,
            "risk_score": self.risk_score,
            "fraud_flag": self.fraud_flag,
            "subscription_id": self.subscription_id,
            "subscription_frequency": self.subscription_frequency,
            "shipments": [s.to_dict() for s in self.shipments],
            "status_history": self.status_history,
            "tracking_number": self.tracking_number,
            "shipping_provider": self.shipping_provider,
            "shipping_address": self.shipping_address.to_dict() if self.shipping_address else None,
            "billing_address": self.billing_address.to_dict() if self.billing_address else None
        }

    @classmethod
    def from_dict(cls, data):
        cust = Customer.from_dict(data["customer"])
        items = [OrderItem.from_dict(i) for i in data["line_items"]]

        shipping_addr = None
        if data.get("shipping_address"):
            shipping_addr = Address.from_dict(data["shipping_address"])

        billing_addr = None
        if data.get("billing_address"):
            billing_addr = Address.from_dict(data["billing_address"])

        coupon_codes = cls._normalise_coupon_codes(data.get("coupon_codes", []))

        shipments_list = []
        if "shipments" in data:
            for sdict in data["shipments"]:
                shipments_list.append(ShipmentRecord.from_dict(sdict))

        obj = cls(
            customer=cust,
            line_items=items,
            payment_info=data["payment_info"],
            pet_name=data["pet_name"],
            shipping_address=shipping_addr,
            billing_address=billing_addr,
            coupon_codes=coupon_codes,
            shipping_speed=data.get("shipping_speed"),
            shipping_cost=data.get("shipping_cost", 0.0),
            fulfillment_center=data.get("fulfillment_center"),
            timestamp=data.get("timestamp"),
            shipping_status=data.get("shipping_status", "Pending"),
            expected_delivery_date=data.get("expected_delivery_date"),
            delivery_date=data.get("delivery_date"),
            refunded=data.get("refunded", "no"),
            delivered=data.get("delivered", "no"),
            payment_status=data.get("payment_status", "authorized"),
            payment_method=data.get("payment_method", "credit_card"),
            partial_refund_amount=data.get("partial_refund_amount", 0.0),
            tax_rate=data.get("tax_rate", 0.0),
            tax_amount=data.get("tax_amount", 0.0),
            env_fee=data.get("env_fee", 0.0),
            currency=data.get("currency", "USD"),
            exchange_rate=data.get("exchange_rate", 1.0),
            loyalty_points_used=data.get("loyalty_points_used", 0),
            loyalty_tier=data.get("loyalty_tier", "None"),
            risk_score=data.get("risk_score", 0),
            fraud_flag=data.get("fraud_flag", False),
            subscription_id=data.get("subscription_id"),
            subscription_frequency=data.get("subscription_frequency")
        )
        obj.order_id = data["order_id"]
        obj.status_history = data.get("status_history", [])
        obj.tracking_number = data.get("tracking_number")
        obj.shipping_provider = data.get("shipping_provider")
        obj.shipments = shipments_list
        return obj