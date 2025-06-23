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
    """
    Generates orders and returns them as a list of dicts.
    We return dict because Celery needs serializable results.
    
    NOTE: This task generates its own random customers for each order,
    so orders from this task do NOT necessarily share customers with clickstream.
    """
    orders = generator.generate_multiple_orders(count)
    return [o.to_dict() for o in orders]

@celery_app.task
def generate_clickstream_task(count):
    """
    Generates clickstream events and returns them as a list of dicts.
    Each event is random/fake, similar in spirit to the orders data generation.
    
    NOTE: This task generates its own random customers for each clickstream event,
    so events from this task do NOT necessarily share customers with orders.
    """
    events = generator.generate_multiple_clickstream_events(count)
    return events

@celery_app.task
def generate_combined_data_task(count):
    """
    NEW TASK:
    Dynamically generate BOTH orders and clickstream events for the SAME customers.
    Returns a dict containing a list of orders and a list of clickstream events.
    """
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
