class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")

    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")

    def make_sound(self):
        print(f"{self.name} the {self.species} makes a generic animal sound.")

    def __str__(self):
        return f"{self.species} named {self.name}"

class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Fish")
        self.age = age

    def swim(self):
        print(f"{self.name} is swimming.")

    def make_sound(self):
        print(f"{self.name} doesn't make much noise but bubbles underwater!")

    def __str__(self):
        return f"Fish named {self.name}, Age: {self.age}"

class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name, "Bird")
        self.wing_span = wing_span  

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wing_span} cm.")

    def make_sound(self):
        print(f"{self.name} chirps melodiously.")

    def __str__(self):
        return f"Bird named {self.name}, Wing Span: {self.wing_span} cm"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking: Woof! Woof!")

    def make_sound(self):
        self.bark()

    def walk(self):
        print(f"{self.name} is walking happily.")

    def __str__(self):
        return f"Dog named {self.name}, Breed: {self.breed}"


dog = Dog("Beethoven", "Daloris")
fish = Fish("Doris", 2)
bird = Bird("AngryBird", 25)

print(dog)
dog.eat()
dog.walk()
dog.make_sound()

