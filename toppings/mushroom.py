from toppings.base_toppings import BaseToppings

class Mushroom(BaseToppings):
    def get_cost(self):
        return 7.99

    def finish_pizza(self):
        print(f"Finishing {self.pizza._order_name}'s {self.pizza._size} pizza with mushrooms")
        print(f"One mushroom pizza coming up!")