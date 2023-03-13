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

#--------------------------------------------

class ServerManagement:
    def __init__(self, server_name):
        self.server_name = server_name

    def start_server(self):
        print(f'Starting server: {self.server_name}')

    def stop_server(self):
        print(f'Stopping server: {self.server_name}')

    def check_status(self):
        print(f'Checking status of server: {self.server_name}')

    def perform_system_updates(self):
        print(f'Performing system updates on server: {self.server_name}')


x = ServerManagement('server1')

x.start_server() # Output: Starting server: server1
x.stop_server() # Output: Stopping server: server1
x.check_status() # Output: Checking status of server: server1
x.perform_system_updates() # Output: Performing system updates on server: server1

x2 = ServerManagement('server2')

x2.start_server() # Output: Starting server: server2
x2.stop_server() # Output: Stopping server: server2
x2.check_status() # Output: Checking status of server: server2
x2.perform_system_updates() # Output: Performing system updates on server: server2

class Deployment:
    def __init__(self, app_name):
        self.app_name = app_name

    def deploy_new_version(self, version):
        print(f'Deploying new version {version} of app: {self.app_name}')

    def rollback_to_previous_version(self, version):
        print(f'Rolling back to previous version {version} of app: {self.app_name}')

    def monitor_deployment_status(self):
        print(f'Monitoring deployment status of app: {self.app_name}')

class InfrastructureProvisioning:
    def __init__(self, environment):
        self.environment = environment

    def provision_new_vm(self, vm_name):
        print(f'Provisioning new virtual machine: {vm_name} in environment: {self.environment}')

    def configure_load_balancer(self, lb_name):
        print(f'Configuring load balancer: {lb_name} in environment: {self.environment}')

    def create_database(self, db_name):
        print(f'Creating database: {db_name} in environment: {self.environment}')


import os
import shutil

class Backup:
    def __init__(self, src_path, dest_path):
        self.src_path = src_path
        self.dest_path = dest_path

    def create_backup(self):
        try:
            shutil.copytree(self.src_path, self.dest_path)
            print(f'Successfully created backup at {self.dest_path}')
        except Exception as e:
            print(f'Error creating backup: {e}')

    def delete_backup(self):
        try:
            shutil.rmtree(self.dest_path)
            print(f'Successfully deleted backup at {self.dest_path}')
        except Exception as e:
            print(f'Error deleting backup: {e}')

import boto3

class EC2Instance:
    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.ec2 = boto3.resource('ec2')

    def start(self):
        try:
            instance = self.ec2.Instance(self.instance_id)
            instance.start()
            print(f'Started instance {self.instance_id}')
        except Exception as e:
            print(f'Error starting instance: {e}')

    def stop(self):
        try:
            instance = self.ec2.Instance(self.instance_id)
            instance.stop()
            print(f'Stopped instance {self.instance_id}')
        except Exception as e:
            print(f'Error stopping instance: {e}')

# Example usage:
instance = EC2Instance('i-0123456789abcdef')
instance.start()
instance.stop()

#--------------------------------------------

import paramiko

class SSHClient:
    def __init__(self, hostname, username, password=None, key_filename=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.client = paramiko.SSHClient()

    def connect(self):
        try:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if self.password:
                self.client.connect(self.hostname, username=self.username, password=self.password)
            else:
                self.client.connect(self.hostname, username=self.username, key_filename=self.key_filename)
            print(f'Connected to {self.hostname}')
        except Exception as e:
            print(f'Error connecting to {self.hostname}: {e}')

    def run_command(self, command):
        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            if error:
                print(f'Error running command: {error}')
            else:
                print(output)
        except Exception as e:
            print(f'Error running command: {e}')

    def close(self):
        self.client.close()
        print(f'Connection to {self.hostname} closed')

# Example usage:
ssh = SSHClient('example.com', 'user', password='secret')
ssh.connect()
ssh.run_command('ls -la')
ssh.close()

