#coding:utf-8
#定义一个用于创建对象的接口，让子类决定实例化哪一个类。工厂方法使一个类的实例化延迟到其子类。
#Description:
    #1. 定义一个抽象的工厂接口类
    #2. 定义一个抽象的产品接口类
    #3. 根据需要从产品接口派生产品子类
    #4. 对于每一个产品子类，从工厂接口派生工厂子类，负责该产品的创建
    #5. 客户端根据实际需要，调用工厂子类，创建所需要的产品。
# Elements:

class Animal(object):
    def eat(self, food):
        raise NotImplementedError()

class Dog(Animal):
    def eat(self, food):
        print 'Dog eat ', food

class Cat(Animal):
    def eat(self, food):
        print 'Cat eat ', food

class AnimalFactory(object):
    def create_animal(self):
        raise NotImplementedError()

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

def client():
    animal_factory = DogFactory()
    animal = animal_factory.create_animal()
    animal.eat('Meat Bones')

    animal_factory = CatFactory()
    animal = animal_factory.create_animal()
    animal.eat('Fish Bones')

if __name__ == '__main__':
    client()
    
"""
class GreekGetter(object):

    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):

    """Simply echoes the msg ids"""

    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()


# Create our localizers
e, g = get_localizer(language="English"), get_localizer(language="Greek")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))

### OUTPUT ###
# dog σκύλος
# parrot parrot
# cat γάτα
# bear bear
"""