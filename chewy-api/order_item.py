from product import Product

class OrderItem:

    def __init__(self, product: Product, quantity: int, free_qty: int = 0):
        self.product = product
        self.quantity = quantity
        self.free_qty = free_qty

    def to_dict(self) -> dict:
        return {
            "product": self.product.to_dict(),
            "quantity": self.quantity,
            "free_qty": self.free_qty
        }

    @classmethod
    def from_dict(cls, data: dict) -> "OrderItem":
        product_obj = Product.from_dict(data["product"])
        return cls(
            product=product_obj,
            quantity=data["quantity"],
            free_qty=data.get("free_qty", 0)
        )