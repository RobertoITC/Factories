from station.cooking_station import CookingStation
from station.delivery_station import DeliveryStation
from models.pizza import Pizza

pizzas=[
    Pizza("Robert","small"),
    Pizza("Benja", "medium"),
    Pizza("Hannia", "large"),
    Pizza("Yair", "small"),
    Pizza("Daniel", "medium"),
]

toppings = ["pepperoni", "meats", "mushroom", "hawaian", "pepperoni"]

deliveries = ["pickup", "delivery", "pickup", "delivery", "pickup"]

for i in range(len(pizzas)):
    pizza_instance = CookingStation.cooking_pizza(toppings[i], pizzas[i])
    pizza_instance_delivery = DeliveryStation.deliver_pizza(deliveries[i], pizzas[i])
    pizza_instance.finish_pizza()
    pizza_instance_delivery.deliver_pizza()
    print(f"Total cost: ${pizzas[i].calculate_pizza_cost_total(pizza_instance, pizza_instance_delivery)}\n")
