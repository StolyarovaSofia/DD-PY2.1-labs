import doctest
class Clothes:
    def __init__(self, seasons: str, cost: float):
        self.seasons = seasons
        self.cost = cost
        """
        :param seasons: Сезон, для которого предназначена одежда 
        (лето, осень и т.д)
        :param cost: Стоимость одежды
        """

    def buy(self, price: float) -> None:
        ...
        """
            Покупка одежды
            :param price: Бюджет
            raise ValueError: Если бюджет меньше стоимости
        то возвращается ошибка.
            """

    def wash(self) -> bool:
        ...
        """
            Стирать в машинке или только ручная стирка
            """
class Flowers:
    def __init__(self, type: str, cost: float):
        self.type = type
        self.cost = cost

    def buy(self, price: float) -> None:
        ...
        """
            Покупка 
            :param price: Бюджет
            raise ValueError: Если бюджет меньше стоимости
           то возвращается ошибка.
            """

    def plant(self) -> bool:
        ...
        """
            Цветет или не цветет
            """

class Animal:
    def eat(self) -> bool:
        ...
        """
            Хищники или травоядные  
            """

    def sleep(self, time: int) -> None:
        ...
        """
            Сон 
            :param time: длительность сна
            """

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
