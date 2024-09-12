# 3. Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income.update({"wage": self.wage})
        self._income.update({"bonus": self.bonus})


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


p = Position("Ivan", "Ivanov", "Director", 100000, 50000)
p.get_full_name()
print(p.get_total_income())
