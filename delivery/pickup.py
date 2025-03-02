from delivery.base_delivery import BaseDelivery

class Pickup(BaseDelivery):
    def get_delivery_cost(self):
        return 0

    def deliver_pizza(self):
        print(f"Order for {self.pizza._order_name} is ready for pickup!")
        print(f"Pick up your {self.pizza._size} pizza at the store!")