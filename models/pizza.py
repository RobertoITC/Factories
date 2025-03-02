
class Pizza:
    def __init__(self, order_name,size):
        self._order_name = order_name
        self._size = size
        self._base_cost = 0


    def calculate_pizza_cost_total(self,topping,delivery):
        if self._size == "small":
            self._base_cost = 10.99
        elif self._size == "medium":
            self._base_cost = 12.99
        elif self._size == "large":
            self._base_cost = 14.99

        delivery_cost = delivery.get_delivery_cost()

        topping_cost = topping.get_cost()

        return self._base_cost + topping_cost + delivery_cost


