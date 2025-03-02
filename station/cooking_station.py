class CookingStation:
    @staticmethod
    def cooking_pizza(topping, pizza):
        if topping == "pepperoni":
            from toppings.pepperoni import Pepperoni
            return Pepperoni(pizza)
        elif topping == "meats":
            from toppings.meats import Meats
            return Meats(pizza)
        elif topping == "mushroom":
            from toppings.mushroom import Mushroom
            return Mushroom(pizza)
        elif topping == "hawaian":
            from toppings.hawaian import Hawaian
            return Hawaian(pizza)
        else:
            raise ValueError("Invalid topping")