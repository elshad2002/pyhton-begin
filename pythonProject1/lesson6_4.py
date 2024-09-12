#4. Реализуйте базовый класс Car.
#● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
#также методы: go, stop, turn(direction), которые должны сообщать, что машина
#поехала, остановилась, повернула (куда);
#● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#● добавьте в базовый класс метод show_speed, который должен показывать текущую
#скорость автомобиля;
#● для классов TownCar и WorkCar переопределите метод show_speed. При значении
#скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
#превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
#выведите результат. Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self. name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"speed = {self.speed}km/h")

    def go(self):
        print("Start")

    def stop(self):
        print("stop")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Speed to bigger. Your speed - {self.speed}km/h")
        else:
            print(f"speed - {self.speed}km/h")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Speed to bigger. Your speed - {self.speed}km/h")
        else:
            print(f"speed - {self.speed}km/h")

class PoliceCar(Car):
    pass

c = Car(100, "green", "mercedes", False)
c.show_speed()
c.turn("Вправо")
print(c.is_police)

t = TownCar(62, "green", "bmw", False)
t.show_speed()
t.turn("Вправо")
print(t.is_police)

w = WorkCar(39, "green", "mercedes", False)
w.show_speed()
w.turn("Вправо")
print(w.is_police)

p = PoliceCar(100, "green", "mercedes", True)
p.show_speed()
p.turn("Вправо")
print(p.is_police)


