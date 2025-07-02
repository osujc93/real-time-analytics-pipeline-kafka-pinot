import uuid

class Customer:
    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        address: str,
        city: str,
        state: str,
        zipcode: str,
    ):
        self.customer_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def to_dict(self) -> dict:
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Customer":
        obj = cls(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            address=data["address"],
            city=data["city"],
            state=data["state"],
            zipcode=data["zipcode"]
        )
        obj.customer_id = data["customer_id"]
        return obj