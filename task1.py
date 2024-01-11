class Animal:
    def __init__(self, name):
        self.name = name

    def makesound(self):
        print("Generic animal sound")


class Dog(Animal):
    def makesound(self):
        print(f" {self.name} : Bark")


class Cat(Animal):
    def makesound(self):
        print(f" {self.name} : Meow")

def animalSound(object1,object2):
    object1.makesound()
    object2.makesound()



myDog = Dog("dog")
myCat = Cat("cat")

animalSound(myDog,myCat)


