class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


person1 = Person("Alice", 30)
person1.say_hello()
# Output:
# Hello, my name is Alice and I'm 30 years old.

person2 = Person("Bob", 25)
person2.say_hello()

# Output:
# Hello, my name is Bob and I'm 25 years old.

#Encapsulation: Classes allow us to group related data and behavior together into a single unit. This makes it easier to manage complexity and to organize our code.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount} into account {self.__account_number}.")

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount} from account {self.__account_number}.")

    def get_balance(self):
        return self.__balance

account = BankAccount("123456", 1000)

account.deposit(500)          # Output: Deposited 500 into account 123456.
account.withdraw(2000)        # Output: Insufficient funds.
account.withdraw(500)         # Output: Withdrew 500 from account 123456.
print(account.get_balance())  # Output: 1000

# print(account.__balance)      # Output: AttributeError: 'BankAccount' object has no attribute '__balance'


#Inheritance: Classes can inherit attributes and methods from other classes. This allows us to create more specialized classes that are based on more general ones.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        print("Meow!")

my_dog = Dog("Fido", "Labrador")
my_cat = Cat("Whiskers", "Orange")

print(my_dog.name)     # Output: Fido
print(my_dog.breed)    # Output: Labrador
my_dog.speak()         # Output: Woof!

print(my_cat.name)     # Output: Whiskers
print(my_cat.color)    # Output: Orange
my_cat.speak()         # Output: Meow!

# When we create a new object of the Dog or Cat class, we first call the __init__ method of the base class (Animal) using the super() function.
# This initializes the name and species attributes of the object.


#Polymorphism: Classes can have the same methods with different implementations. This allows us to write code that works with different types of objects in a consistent way.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Bird(Animal):
    def speak(self):
        return "Chirp"

animals = [Cat("Whiskers"), Dog("Fido"), Bird("Polly")]

for animal in animals:
    print(animal.name + ": " + animal.speak())
