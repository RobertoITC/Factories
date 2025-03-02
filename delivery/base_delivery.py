from abc import ABC, abstractmethod

class BaseDelivery(ABC):
    def __init__(self, pizza):
        self.pizza = pizza

    @abstractmethod
    def get_delivery_cost(self):
        pass

    @abstractmethod
    def deliver_pizza(self):
        pass