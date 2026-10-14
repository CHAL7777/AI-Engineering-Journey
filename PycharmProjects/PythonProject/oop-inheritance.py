class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self.name,"Eat hyena")

class Dog(Animal):
    def bark(self):
        print(self.name,"woooo")

ani=Animal("wolf")
hey=Dog("Dog")

ani.eat()
hey.bark()