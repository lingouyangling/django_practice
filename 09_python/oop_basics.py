class Dog():

    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog(breed = "Lab", name="Sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(20)

print(myc.radius)
print(myc.area())
