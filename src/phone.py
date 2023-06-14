from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, num_sim: int):
        super().__init__(name, price, quantity)
        self.__num_sim = num_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.num_sim})"

    @property
    def num_sim(self):
        return self.__num_sim

    @num_sim.setter
    def num_sim(self, num_sim):
        if num_sim <= 0 or not isinstance(num_sim, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__num_sim = num_sim
