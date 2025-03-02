from toppings.base_toppings import BaseToppings


class Meats(BaseToppings):
    def get_cost(self):
        return 8.99

    def finish_pizza(self):
        print(f"Finishing {self.pizza._order_name}'s {self.pizza._size} pizza with ham, pepperoni, and sausage")
        print(f"One supreme meats pizza coming up!")