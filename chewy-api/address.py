class Address:
    def __init__(self, street: str, city: str, state: str, zipcode: str):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def to_dict(self) -> dict:
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode
        }

    @classmethod
    def from_dict(cls, data) -> "Address":
        return cls(
            street=data["street"],
            city=data["city"],
            state=data["state"],
            zipcode=data["zipcode"]
        )