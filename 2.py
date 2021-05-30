from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        print(f"Consumption of fabric for sewing a coat - {round(self.param / 6.5) + 0.5}")
        return round(self.param / 6.5) + 0.5  # РґР»СЏ __add__


class Costume(Clothes):
    @property
    def consumption(self):
        print(f"Consumption of fabric for sewing a costume - {(2 * self.param + 0.3) / 100}")
        return (2 * self.param + 0.3) / 100


coat = Coat(42)
costume = Costume(170)
print(coat + costume)