import uuid

class Review:

    def __init__(self, customer_id: str, product_id: str, rating: int, comment: str = ""):
        self.review_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.product_id = product_id
        self.rating = rating
        self.comment = comment