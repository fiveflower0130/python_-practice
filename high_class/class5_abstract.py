# python 本身是不能寫abstract class必須使用內建套件
from abc import ABCMeta, abstractmethod, ABC

'''
1.abstract class就是指class是空的每個methods是不帶內容的
2. 一個abstract class至少要有一個abstract method
3. abstract class如果有一個abstract method的話便不能instantiate(實體化)
4. abstract class需要有人去繼承，繼承的class則需要覆寫每一個abstract method
5. abstract class的好處是較常見用在大型專案，在撰寫程式時提供一個藍圖架構並在分工時能給予提醒
'''


class Product(metaclass=ABCMeta):
    @abstractmethod
    def hi(self):
        pass

    @abstractmethod
    def hi2(self):
        pass


class Drink(Product):
    def hi(self):
        print('hi')

    def hi2(self):
        print('hi hi')


# p = Product()
d = Drink()


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print('meow')


class Dog(Animal):
    def make_sound(self):
        print('wan')


class People(Animal):
    def make_sound(self):
        print('hi')


c = Cat()
c.make_sound()
d = Dog()
d.make_sound()
p = People()
p.make_sound()
