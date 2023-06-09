import os
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.abspath(r"../src/items.csv")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) >= 10:
            raise ValueError('длина наименования товара больше 10 символов')
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        with open(cls.CSV_PATH, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string: str):
        """
        Возвращает число из числа-строки
        """
        try:
            return int(string)
        except ValueError:
            return "Невозможно преобразовать в число"
