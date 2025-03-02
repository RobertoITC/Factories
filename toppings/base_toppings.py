from abc import ABC, abstractmethod

class BaseToppings(ABC):
    def __init__(self, pizza):
        self.pizza = pizza

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def finish_pizza(self):
        pass