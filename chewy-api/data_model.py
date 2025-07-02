import uuid
import random
from faker import Faker
from datetime import datetime, timedelta
import string  
import pytz

from location_data import USZipcodeLocationData
from product_catalog import PRODUCT_CATALOG
from product import Product
from customer import Customer
from address import Address
from order_item import OrderItem
from shipment_record import ShipmentRecord
from order import Order
from order_status_history import OrderStatusHistory
from promotions import COUPON_DETAILS


fake = Faker()

FULFILLMENT_CENTERS = [
    "FC_Atlanta",
    "FC_Dallas",
    "FC_LosAngeles",
    "FC_Chicago",
    "FC_Seattle",
    "FC_NewYork",
    "FC_Denver",
    "FC_Miami",
    "FC_Phoenix",
    "FC_Boston",
    "FC_Detroit",
    "FC_Houston",
    "FC_Memphis",
    "FC_Denver",
    "FC_Pittsburgh"
]

CURRENCY_OPTIONS = ["USD", "EUR", "CAD"]
EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 1.07,
    "CAD": 0.75
}

DOG_DRY_VARIANTS = [
    ("7.7_LBS", 39.99),
    ("15.5_LBS", 59.99),
    ("25.5_LBS", 79.99)
]
DOG_CAN_VARIANTS = [
    ("12.5OZ_CASE12", 39.99),
    ("12.5OZ_CASE24", 74.99)
]

CAT_DRY_VARIANTS = [
    ("4.4_LBS", 29.99),
    ("12.2_LBS", 49.99),
    ("19.8_LBS", 64.99)
]
CAT_CAN_VARIANTS = [
    ("5.5OZ_CASE12", 21.99),
    ("5.5OZ_CASE24", 39.99)
]

dog_prescription_keys = []
cat_prescription_keys = []
for sku_key, details in PRODUCT_CATALOG.items():
    if "Prescription Diet" in details["category"] or "Veterinary Diet" in details["category"]:
        if "_DOG_" in sku_key:
            dog_prescription_keys.append(sku_key)
        elif "_CAT_" in sku_key:
            cat_prescription_keys.append(sku_key)

for base_key in dog_prescription_keys:
    base_info = PRODUCT_CATALOG[base_key]
    base_name = base_info["name"]
    base_category = base_info["category"]

    for (suffix, price) in DOG_DRY_VARIANTS:
        new_sku = f"{base_key}_{suffix}"
        PRODUCT_CATALOG[new_sku] = {
            "name": f"{base_name} - Dry {suffix.replace('_', ' ')}",
            "category": base_category,
            "price": price
        }

    for (suffix, price) in DOG_CAN_VARIANTS:
        new_sku = f"{base_key}_CANS_{suffix}"
        PRODUCT_CATALOG[new_sku] = {
            "name": f"{base_name} - Canned {suffix.replace('_', ' ')}",
            "category": base_category,
            "price": price
        }

for base_key in cat_prescription_keys:
    base_info = PRODUCT_CATALOG[base_key]
    base_name = base_info["name"]
    base_category = base_info["category"]

    for (suffix, price) in CAT_DRY_VARIANTS:
        new_sku = f"{base_key}_{suffix}"
        PRODUCT_CATALOG[new_sku] = {
            "name": f"{base_name} - Dry {suffix.replace('_', ' ')}",
            "category": base_category,
            "price": price
        }

    for (suffix, price) in CAT_CAN_VARIANTS:
        new_sku = f"{base_key}_CANS_{suffix}"
        PRODUCT_CATALOG[new_sku] = {
            "name": f"{base_name} - Canned {suffix.replace('_', ' ')}",
            "category": base_category,
            "price": price
        }

class FakeEcommerceDataGenerator:

    def __init__(self):
        self.generated_emails = set()
        self.shipping_providers = ["FedEx", "UPS", "USPS", "DHL"]
        self.generated_tracking_numbers = set() 

        self.ny_tz = pytz.timezone("America/New_York")

    def _generate_tracking_number(self, length: int = 12) -> str:

        while True:
            code = "".join(random.choices(string.ascii_uppercase + string.digits, k=length))
            if code not in self.generated_tracking_numbers:
                self.generated_tracking_numbers.add(code)
                return code
            
    def _get_next_timestamp_str(self):

        now = datetime.now(self.ny_tz)
        return now.strftime("%Y-%m-%dT%H:%M:%S.%f")
            
    def generate_unique_email(self):
        while True:
            candidate = fake.ascii_email()
            if candidate not in self.generated_emails:
                self.generated_emails.add(candidate)
                return candidate

    def generate_customer(self):
        city, state, zipcode, area_code = USZipcodeLocationData.get_random_location()
        name = fake.name()
        address = fake.street_address()
        phone = f"{area_code}-{random.randint(100,999)}-{random.randint(1000,9999)}"
        email = self.generate_unique_email()
        return Customer(name, email, phone, address, city, state, zipcode)

    def generate_address(self):
        city, state, zipcode, _ = USZipcodeLocationData.get_random_location()
        street = fake.street_address()
        return Address(street, city, state, zipcode)

    def generate_payment_info(self):

        if random.random() < 0.5:
            return "4443" + "x" * 8 + "0092"
        else:
            random_prefix = fake.user_name()
            random_domain = fake.domain_name()
            return f"{random_prefix}@{random_domain}"

    def generate_coupon_codes(self):

        possible = list(COUPON_DETAILS.keys())
        random.shuffle(possible)
        num = random.randint(0, 2)
        return possible[:num]

    def generate_pet_name(self):
        return fake.first_name()

    def generate_loyalty_tier(self):
        return random.choice(["None", "Silver", "Gold", "Platinum"])

    def generate_risk_score(self, shipping_address, billing_address):

        risk = random.randint(0, 100)
        if shipping_address and billing_address:
            if shipping_address.city != billing_address.city:
                risk += 20
        return min(risk, 100)

    def generate_partial_shipments(self, order_items):

        shipments = []
        random.shuffle(order_items)

        num_shipments = 1 if random.random() < 0.5 else 2

        if num_shipments == 1:
            shipments.append(ShipmentRecord(items=order_items))
        else:
            mid_point = len(order_items) // 2
            first_list = order_items[:mid_point]
            second_list = order_items[mid_point:]
            shipments.append(ShipmentRecord(items=first_list))
            if second_list:
                shipments.append(ShipmentRecord(items=second_list))

        return shipments

    def decrement_stock(self, product, qty):
        product.stock -= qty
        if product.stock < 0:
            product.out_of_stock = True

    def generate_customer_info(self):

        return self.generate_customer()

    def generate_order(self, customer=None):

        if customer is None:
            customer = self.generate_customer()

        shipping_addr = self.generate_address()
        if random.random() < 0.8:
            billing_addr = shipping_addr
        else:
            billing_addr = self.generate_address()

        num_items = random.randint(1, 7)
        line_items = []
        catalog_keys = list(PRODUCT_CATALOG.keys())

        for _ in range(num_items):
            sku = random.choice(catalog_keys)
            product_data = PRODUCT_CATALOG[sku]
            stock_amt = random.randint(1, 600)
            prod_obj = Product(
                name=product_data["name"],
                category=product_data["category"],
                price=product_data["price"],
                stock=stock_amt
            )
            quantity = random.randint(1, 3)

            if (stock_amt - quantity) < 0:
                partial_qty = max(0, stock_amt)
                item = OrderItem(prod_obj, partial_qty)
                self.decrement_stock(prod_obj, partial_qty)
            else:
                item = OrderItem(prod_obj, quantity)
                self.decrement_stock(prod_obj, quantity)

            line_items.append(item)

        payment_info = self.generate_payment_info()
        coupon_codes = self.generate_coupon_codes()
        pet_name = self.generate_pet_name()

        possible_methods = ["credit_card", "PayPal", "debit_card"]
        payment_method = random.choice(possible_methods)

        possible_pay_status = ["authorized", "captured", "failed", "refunded"]
        payment_status = random.choices(possible_pay_status, weights=[0.5, 0.4, 0.05, 0.05], k=1)[0]

        shipping_speed = random.choice(["Standard", "Express", "Overnight"])
        shipping_cost = round(random.uniform(3.0, 25.0), 2)
        fc = random.choice(FULFILLMENT_CENTERS)

        currency_choice = random.choice(CURRENCY_OPTIONS)
        exchange_rate = EXCHANGE_RATES[currency_choice]

        env_fee = 0.0
        if any("Aquatic" in it.product.category or "Terrarium" in it.product.category for it in line_items):
            env_fee = round(random.uniform(1.0, 5.0), 2)

        tax_rate = round(random.uniform(0.05, 0.10), 2)

        loyalty_tier = self.generate_loyalty_tier()
        loyalty_points_used = 0
        if loyalty_tier in ["Gold", "Platinum"]:
            loyalty_points_used = random.randint(0, 1000)

        subscription_id = subscription_frequency = None
        if random.random() < 0.25:
            subscription_id = str(uuid.uuid4())
            subscription_frequency = random.choice(
                ["every week", "every 2 weeks", "every 4 weeks", "every month", "every 8 weeks"]
            )

        rscore = self.generate_risk_score(shipping_addr, billing_addr)
        fraud_flag = (rscore > 91)

        order_timestamp_str = self._get_next_timestamp_str()
        order_dt = datetime.strptime(order_timestamp_str, "%Y-%m-%dT%H:%M:%S.%f")

        shipping_status = random.choices(
            ["Pending", "Shipped", "Out for Delivery", "Delivered", "Returned", "Lost"],
            weights=[0.3, 0.3, 0.1, 0.25, 0.05, 0.01],
            k=1,
        )[0]

        delivered = "yes" if shipping_status == "Delivered" else "no"
        refunded = "yes" if random.random() < 0.10 else "no"

        expected_delivery_date = None

        delivery_date = None
        if shipping_status in ["Shipped", "Out for Delivery"]:
            expected_delivery_date = (order_dt + timedelta(days=random.randint(1, 4))).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            )[:-3]
        elif shipping_status == "Delivered":
            delivery_date = (order_dt + timedelta(days=random.randint(0, 2))).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            )[:-3]

        partial_refund_amount = round(random.uniform(1.0, 150.0), 2) if refunded == "yes" else 0.0

        order = Order(
            customer=customer,
            line_items=line_items,
            payment_info=payment_info,
            pet_name=pet_name,
            shipping_address=shipping_addr,
            billing_address=billing_addr,
            coupon_codes=coupon_codes,
            shipping_speed=shipping_speed,
            shipping_cost=shipping_cost,
            fulfillment_center=fc,
            timestamp=order_timestamp_str,
            shipping_status=shipping_status,
            expected_delivery_date=expected_delivery_date,
            delivery_date=delivery_date,
            refunded=refunded,
            delivered=delivered,
            payment_status=payment_status,
            payment_method=payment_method,
            partial_refund_amount=partial_refund_amount,
            currency=currency_choice,
            exchange_rate=exchange_rate,
            env_fee=env_fee,
            tax_rate=tax_rate,
            loyalty_points_used=loyalty_points_used,
            loyalty_tier=loyalty_tier,
            risk_score=rscore,
            fraud_flag=fraud_flag,
            subscription_id=subscription_id,
            subscription_frequency=subscription_frequency
        )

        if random.random() < 0.70 or shipping_status != "Pending":
            order.tracking_number = self._generate_tracking_number()
            order.shipping_provider = random.choice(self.shipping_providers)

        shipments = self.generate_partial_shipments(order.line_items)
        for s in shipments:
            if shipping_status == "Delivered":
                s.shipment_status = "Delivered"
                s.shipment_timestamp = delivery_date
            elif shipping_status in ["Shipped", "Out for Delivery"]:
                s.shipment_status = "Shipped"
                s.shipment_timestamp = order_timestamp_str
            else:
                s.shipment_status = shipping_status
            s.tracking_number = order.tracking_number or self._generate_tracking_number()
        order.shipments = shipments

        if refunded == "yes":
            order.status_history.append(OrderStatusHistory("Refunded").to_dict())

        return order

    def generate_clickstream_event(self, customer=None):

        event_time_str = self._get_next_timestamp_str()

        city, state, zipcode, area_code = USZipcodeLocationData.get_random_location()

        ip_address = f"198.{area_code % 256}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        geo_location = f"US-{state}"

        choice_roll = random.random()
        if choice_roll < 0.70:
            product_sku = random.choice(list(PRODUCT_CATALOG.keys()))
            product_info = PRODUCT_CATALOG[product_sku]
            page_name = "ProductDetailPage"
            page_url = (
                f"https://www.blewy.com/p/"
                + product_info["name"].lower().replace(" ", "-").replace("'", "")
                + f"/dp/{product_sku}"
            )
            product_id = product_sku
            product_name = product_info["name"]
            brand_name = "Blewy Brand"
            category_name = product_info["category"]
            price = product_info["price"]
        elif choice_roll < 0.80:
            page_name = "HomePage"
            page_url = "https://www.blewy.com"
            product_id = None
            product_name = None
            brand_name = None
            category_name = None
            price = None
        elif choice_roll < 0.85:
            page_name = "ContactUsPage"
            page_url = "https://www.blewy.com/contact"
            product_id = None
            product_name = None
            brand_name = None
            category_name = None
            price = None
        else:
            page_name = "CategoryPage"
            cat_sku = random.choice(list(PRODUCT_CATALOG.keys()))
            cat_info = PRODUCT_CATALOG[cat_sku]
            cat_slug = cat_info["category"].lower().replace(" ", "-").replace("(", "").replace(")", "")
            page_url = f"https://www.blewy.com/c/{cat_slug}"
            product_id = None
            product_name = None
            brand_name = None
            category_name = cat_info["category"]
            price = None

        event_type = random.choice([
            "page_view",
            "add_to_cart",
            "checkout",
            "search",
            "product_impression",
            "remove_from_cart"
        ])

        quantity = 1
        if event_type in ["add_to_cart", "remove_from_cart", "checkout"] and page_name == "ProductDetailPage":
            quantity = random.randint(1, 3)

        if customer is not None:
            user_id = customer.customer_id
        else:
            user_id = f"user-{random.randint(1000, 9999)}"

        session_id = f"sess-{uuid.uuid4()}"

        possible_referrers = [
            "https://www.google.com",
            "https://www.yahoo.com",
            "https://www.duckduckgo.com",
            "https://www.petsmart.com",
            "https://www.vetsource.com",
            "https://www.chewy.com",
            "https://www.amazon.com",
            "direct",
            "https://www.bing.com",
        ]
        referrer_url = random.choice(possible_referrers)

        user_login_status = random.choice(["logged_in", "guest"])
        loyalty_status = random.choice(["none", "silver", "gold", "platinum"])
        pet_pref = random.choice(["dog", "cat", "bird", "fish", "small_pet", "horse"])

        possible_campaigns = ["springsale-2025", "wintersale-2024", "emailpromo123", "none"]
        marketing_campaign_id = random.choice(possible_campaigns)
        if marketing_campaign_id == "none":
            marketing_campaign_id = None

        device_type = random.choice(["desktop", "mobile", "tablet"])
        browser_name = random.choice(["Chrome", "Firefox", "Safari", "Edge", "IE"])
        os_version = random.choice(["Windows 11", "MacOS 13", "iOS 16", "Android 12", "Linux"])
        app_version = None
        if device_type in ["mobile", "tablet"] and random.random() < 0.5:
            app_version = f"{random.randint(1, 3)}.{random.randint(0,9)}.{random.randint(0,9)}"

        language_pref = random.choice(["en-US", "en-GB", "es-ES", "fr-FR", "de-DE", "it-IT"])

        search_query = None
        search_results_count = None
        filters_applied = []
        if event_type == "search":
            search_query = random.choice(["plush dog toy", "cat food", "fish tank filter", "dog treats"])
            search_results_count = random.randint(10, 500)
            if random.random() < 0.5:
                filters_applied.append("size:medium")
            if random.random() < 0.3:
                filters_applied.append("material:plush")
            if random.random() < 0.2:
                filters_applied.append("flavor:chicken")

        cart_id = None
        cart_value_before_event = None
        cart_value_after_event = None
        if event_type in ["add_to_cart", "checkout", "remove_from_cart"]:
            cart_id = f"cart-{random.randint(1000, 9999)}"
            base_val = round(random.uniform(5.0, 100.0), 2)
            cart_value_before_event = base_val
            if event_type == "remove_from_cart":
                cart_value_after_event = round(base_val - random.uniform(1, 10), 2)
            else:
                cart_value_after_event = round(base_val + random.uniform(5, 20), 2)

        time_spent_on_page_ms = random.randint(500, 20000)
        promotion_code = None
        if random.random() < 0.2:
            promotion_code = random.choice(list(COUPON_DETAILS.keys()))
        page_load_time_ms = random.randint(100, 5000)
        customer_support_chat_opened = random.random() < 0.05

        evt = {
            "event_id": f"evt-{uuid.uuid4()}",
            "timestamp": event_time_str,
            "user_id": user_id,
            "session_id": session_id,
            "event_type": event_type,
            "page_url": page_url,
            "page_name": page_name,
            "referrer_url": referrer_url,
            "product_id": product_id,
            "product_name": product_name,
            "brand_name": brand_name,
            "category_name": category_name,
            "price": price,
            "quantity": quantity,
            "user_login_status": user_login_status,
            "loyalty_status": loyalty_status,
            "pet_preference": pet_pref,
            "marketing_campaign_id": marketing_campaign_id,
            "device_type": device_type,
            "browser_name": browser_name,
            "app_version": app_version,
            "os_version": os_version,
            "ip_address": ip_address,
            "geo_location": geo_location,
            "language_pref": language_pref,
            "search_query": search_query,
            "search_results_count": search_results_count,
            "filters_applied": filters_applied,
            "cart_id": cart_id,
            "cart_value_before_event": cart_value_before_event,
            "cart_value_after_event": cart_value_after_event,
            "metadata": {
                "is_first_visit": (random.random() < 0.3),
                "time_spent_on_page_ms": time_spent_on_page_ms,
                "promotion_code": promotion_code,
                "page_load_time_ms": page_load_time_ms,
                "customer_support_chat_opened": customer_support_chat_opened
            }
        }
        return evt

    def generate_multiple_clickstream_events(self, count, customer=None):

        if customer is None:
            customer = self.generate_customer_info()
        return [self.generate_clickstream_event(customer=customer) for _ in range(count)]

    def generate_multiple_orders(self, count, customer=None):

        if customer is None:
            customer = self.generate_customer_info()
        return [self.generate_order(customer=customer) for _ in range(count)]