class Tomato:
    type = {1: "Зеленая", 2: "Молочная", 3: "Бурая", 4: "Розовая", 5: "Красная"}

    def __init__(self, index: int = 1) -> None:
        self._index = index
        self._state = self.type.get(1)

    def grow(self) -> None:
        if self._index < len(self.type):
            self._index += 1
            self._state = self.type.get(self._index)

    def is_ripe(self) -> bool:
        return self._state == self.type.get(len(self.type)

class TomatoBush:
    def __init__(self, tomatoes_count: int) -> None:
        self.tomatoes = [Tomato() for _ in range(tomatoes_count)]

    def grow_all(self) -> None:
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self) -> bool:
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self) -> None:
        if self.all_are_ripe():
            self.tomatoes.clear()


class Gardener:
    def __init__(self, name: str, plant: TomatoBush) -> None:
        self.name = name
        self._plant = plant

    def work(self) -> None:
        self._plant.grow_all()

    def harvest(self) -> None:
        if self._plant.all_are_ripe():
            print("Все плоды созрели")
            self._plant.give_away_all()
            print("Урожай собран")
        else:
            print("Не все плоды созрели")

    @staticmethod
    def knowledge_base() -> str:
        return "Ухаживайте за кустом, чтобы томаты созрели"


if __name__ == "__main__":
    print(Gardener.knowledge_base())
    tomato_bush = TomatoBush(10)
    gardener = Gardener("John", tomato_bush)
    gardener.work()
    gardener.harvest()
    while tomato_bush.all_are_ripe() == False:
        gardener.work()
        gardener.harvest()
