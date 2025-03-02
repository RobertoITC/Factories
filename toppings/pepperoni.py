from toppings.base_toppings import BaseToppings

class Pepperoni(BaseToppings):
    def get_cost(self):
        return 6.99

    def finish_pizza(self):
        print(f"Finishing {self.pizza._order_name}'s {self.pizza._size} pizza with pepperoni")
        print(f"One pepperoni pizza coming up!")