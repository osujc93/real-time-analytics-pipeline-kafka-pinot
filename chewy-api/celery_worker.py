from celery import Celery
from data_model import FakeEcommerceDataGenerator
from location_data import USZipcodeLocationData

celery_app = Celery(
    "celery_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

USZipcodeLocationData.init_uszipcode_data()

generator = FakeEcommerceDataGenerator()

@celery_app.task
def generate_orders_task(count):

    orders = generator.generate_multiple_orders(count)
    return [o.to_dict() for o in orders]

@celery_app.task
def generate_clickstream_task(count):

    events = generator.generate_multiple_clickstream_events(count)
    return events

@celery_app.task
def generate_combined_data_task(count):

    orders_list = []
    events_list = []

    for _ in range(count):
        cust = generator.generate_customer_info()

        order_obj = generator.generate_order(customer=cust)
        orders_list.append(order_obj.to_dict())

        click_evt = generator.generate_clickstream_event(customer=cust)
        events_list.append(click_evt)

    return {
        "orders": orders_list,
        "clickstream": events_list
    }
