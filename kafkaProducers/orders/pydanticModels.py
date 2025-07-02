#!/usr/bin/env python3

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, model_validator  

class BillingAddress(BaseModel):
    city: str
    state: str
    street: str
    zipcode: str


class ShippingAddress(BaseModel):
    city: str
    state: str
    street: str
    zipcode: str


class StatusHistoryItem(BaseModel):
    status: str
    status_id: str
    timestamp: str


class LineItemProduct(BaseModel):
    category: str
    name: str
    out_of_stock: bool
    price: float
    product_id: str
    stock: int


class LineItem(BaseModel):
    free_qty: int
    product: LineItemProduct
    quantity: int


class CouponCodes(BaseModel):
    name: str    


class ShipmentItemProduct(BaseModel):
    category: str
    name: str
    out_of_stock: bool
    price: float
    product_id: str
    stock: int


class ShipmentItem(BaseModel):
    free_qty: int
    product: ShipmentItemProduct
    quantity: int


class Shipment(BaseModel):
    items: List[ShipmentItem]
    shipment_id: str
    shipment_status: str
    shipment_timestamp: Optional[Union[str, None]]
    tracking_number: Optional[Union[str, None]]


class Customer(BaseModel):
    address: str
    city: str
    customer_id: str
    email: str
    name: str
    phone: str
    state: str
    zipcode: str


class EcommOrder(BaseModel):
    billing_address: BillingAddress
    coupon_codes: List[CouponCodes]
    currency: str
    customer: Customer
    delivered: str
    delivery_date: Optional[str]
    env_fee: float
    exchange_rate: float
    expected_delivery_date: Optional[str]
    fraud_flag: bool
    fulfillment_center: str
    line_items: List[LineItem]
    loyalty_points_used: int
    loyalty_tier: str
    order_id: str
    order_total: float
    partial_refund_amount: float
    payment_info: str
    payment_method: str
    payment_status: str
    pet_name: str
    refunded: str
    risk_score: int
    shipments: List[Shipment]
    shipping_address: ShippingAddress
    shipping_cost: float
    shipping_provider: Optional[str]
    shipping_speed: str
    shipping_status: str
    status_history: List[StatusHistoryItem]
    subscription_frequency: Optional[str]
    subscription_id: Optional[str]
    subtotal_after_coupon: float
    subtotal_before_promos: float
    tax_amount: float
    tax_rate: float
    timestamp: str
    tracking_number: Optional[str]
    
class OrdersApiResponse(BaseModel):
    data: List[EcommOrder]
    page: int
    total_pages: int

    @model_validator(mode='after')
    def skip_no_data(cls, instance: "OrdersApiResponse") -> "OrdersApiResponse":

        # Ensure each EcommOrder has a non-empty line_items list
        for idx, rs in enumerate(instance.data):
            if not rs.line_items:
                raise ValueError(
                    f"Invalid record: data[{idx}].line_items is empty."
                )

        # If all checks pass, return the instance
        return instance

