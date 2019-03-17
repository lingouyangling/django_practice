class Animal():

    def __init__(self):
        print("animal created")

    def whoami(self):
        print('animal')

    def eat(self):
        print('eating')

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print('dog created')

    def bark(self):
        print('woof')

    def eat(self):
        print('dog eating')

# mya = Animal()
# mya.whoami()
# mya.eat()

mydog = Dog()
mydog.whoami()
mydog.eat()
mydog.bark()
