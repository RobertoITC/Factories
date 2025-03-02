class DeliveryStation:
    @staticmethod
    def deliver_pizza(method, pizza):
        if method == "delivery":
            from delivery.takeout import TakeOut
            return TakeOut(pizza)
        elif method == "pickup":
            from delivery.pickup import Pickup
            return Pickup(pizza)
        else:
            raise ValueError("Invalid delivery method")