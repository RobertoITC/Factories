from delivery.base_delivery import BaseDelivery

class TakeOut(BaseDelivery):
    def get_delivery_cost(self):
        return 1.99

    def deliver_pizza(self):
        print(f"Order for {self.pizza._order_name} is ready for delivery!")
        print(f"Delivering {self.pizza._size} pizza!")