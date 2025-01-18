def add(*args):
    #   The args argument stores values as a tuple
    #   print(args)

    total = 0
    for n in args:
        total += n
    return total


def calculate(**kwargs):
    #  The kwarg inputs are stored as an input
    # for key, value in kwargs.items():
    #       print(key)
    pass


calculate(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
