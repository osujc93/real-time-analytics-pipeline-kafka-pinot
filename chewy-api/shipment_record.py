import uuid
from typing import List
from order_item import OrderItem

class ShipmentRecord:

    def __init__(
        self,
        items: List[OrderItem],
        tracking_number: str | None = None,
        shipment_status: str = "Pending",
    ):
        self.shipment_id = str(uuid.uuid4())
        self.items = items
        self.tracking_number = tracking_number
        self.shipment_status = shipment_status
        self.shipment_timestamp = None

    def to_dict(self) -> dict:
        return {
            "shipment_id": self.shipment_id,
            "items": [i.to_dict() for i in self.items],
            "tracking_number": self.tracking_number,
            "shipment_status": self.shipment_status,
            "shipment_timestamp": self.shipment_timestamp
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ShipmentRecord":
        items = [OrderItem.from_dict(x) for x in data["items"]]
        obj = cls(
            items=items,
            tracking_number=data["tracking_number"],
            shipment_status=data["shipment_status"]
        )
        obj.shipment_id = data["shipment_id"]
        obj.shipment_timestamp = data.get("shipment_timestamp")
        return obj