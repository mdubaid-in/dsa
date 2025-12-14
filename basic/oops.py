print("-" * 100)
print("OOPs")
print("-" * 100)


class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)  # (Instance variable)
print(dog2.name)  # (Instance variable)

# Modify instance variables
dog1.name = "Max"
dog1.species = "German Shepherd"
print(dog1.name)  # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)

# --------------------------------------------------------------------------------- #
print("-" * 100)
print("Inheritance")
print("-" * 100)


# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")


class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")


# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")


# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")


class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")


# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()

# --------------------------------------------------------------------------------- #
print("-" * 100)
print("Polymorphism")
print("-" * 100)


class Calculator:
    def add(self, *args):
        return sum(args)


calc = Calculator()
print(calc.add(5, 10))  # Two arguments
print(calc.add(5, 10, 15))  # Three arguments
print(calc.add(1, 2, 3, 4))


# Method Overriding
# We start with a base class and then a subclass that "overrides" the speak method.
class Animal:
    def speak(self):
        return "I am an animal."


class Dog(Animal):
    def speak(self):
        return "Woof!"


print(Dog().speak())


# 2 Duck Typing
class Cat:
    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    # This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()


print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))


# 3 Operator Overloading
# We create a simple class that customizes the '+' operator.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # This special method defines the behavior of the '+' operator.
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v3)

# --------------------------------------------------------------------------------- #
print("-" * 100)
print("Encapsulation")
print("-" * 100)


class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())


# --------------------------------------------------------------------------------- #
print("-" * 100)
print("Abstraction")
print("-" * 100)

from abc import ABC, abstractmethod


class Dog(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Dog's Name: {self.name}")


class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")


class Beagle(Dog):  # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")


# Example Usage
dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method
    dog.sound()  # Calls implemented abstract method
