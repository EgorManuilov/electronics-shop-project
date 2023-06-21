import self as self

from src.item import Item


class MixinLangChange:
    def __init__(self, language="EN"):
        self.language = language

    def language(self):
        return self.language

    def change_lang(self):

        """
        Метод для изменения языка
        """

        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        return self


class KeyBoard(Item, MixinLangChange):
    """
    Класс `Keyboard` для товара 'клавиатура',
    атрибут `language`
    и метод для изменения языка (раскладки клавиатуры)
    """

    def __init__(self, name, price, quantity, language="EN"):
        MixinLangChange.__init__(self, language)
        Item.__init__(self, name, price, quantity)

    def __str__(self):
        return f"{self.name}"
