import uuid

class Product:
    def __init__(self, name: str, category: str, price: float, stock: int):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.out_of_stock = False

    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock,
            "out_of_stock": self.out_of_stock
        }

    @classmethod
    def from_dict(cls, data) -> "Product":
        obj = cls(
            name=data["name"],
            category=data["category"],
            price=data["price"],
            stock=data["stock"]
        )
        obj.product_id = data["product_id"]
        obj.out_of_stock = data.get("out_of_stock", False)
        return obj