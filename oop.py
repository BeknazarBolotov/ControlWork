class Person:

    def __init__(self, age=0):
        self._age = None
        self.set_age(age)

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self._age = age

    def get_age(self):
        return self._age

person = Person()
person.set_age(25)
print(person.get_age())



class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal.")



class Dog(Animal):

    def speak(self):
        return "WOOF!"



class Cat(Animal):

    def speak(self):
        return "MeoW ^_^"



dog = Dog("Sharik")
cat = Cat("Kefir")

print(dog.name, dog.speak())
print(cat.name, cat.speak())



class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    print(vehicle.move())

car = Car()
bike = Bicycle()
move(car)
move(bike)


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


rectangle = Rectangle(10, 5)
circle = Circle(7)
print(rectangle.area())
print(circle.area())


