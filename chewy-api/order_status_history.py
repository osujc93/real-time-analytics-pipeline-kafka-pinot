import uuid
from datetime import datetime

class OrderStatusHistory:

    def __init__(self, status: str, timestamp: str | None = None):
        self.status_id = str(uuid.uuid4())
        self.status = status
        self.timestamp = timestamp or datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    def to_dict(self) -> dict:
        return {
            "status_id": self.status_id,
            "status": self.status,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data: dict) -> "OrderStatusHistory":
        obj = cls(
            status=data["status"],
            timestamp=data["timestamp"]
        )
        obj.status_id = data["status_id"]
        return obj