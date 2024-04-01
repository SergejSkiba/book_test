#0
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

#9.1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant", self.restaurant_name, "is now open!")

restaurant0 = Restaurant("Sunny's Cafe", "Italian")
print("Restaurant name:", restaurant0.restaurant_name)
print("Cuisine type:", restaurant0.cuisine_type)

#9.2
restaurant1 = Restaurant("Sunny's Cafe", "Italian")
restaurant2 = Restaurant("Bulbian", "Belarusian")
restaurant3 = Restaurant("Green Leaf", "Vegetarian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9.3
class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print("User information:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Email:", self.email)

    def greet_user(self):
        print("Hello,", self.first_name + "!")

user1 = User("Sergey", "Skiba", 40, "skiba.sergej1981gmail.com")
user1.describe_user()
user1.greet_user()

#0
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        print(f"The mileage of this car {self.odometer_reading} miles.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


#9.4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant", self.restaurant_name, "is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant0 = Restaurant("Sunny's Cafe", "Italian")
restaurant0.set_number_served(10)
print("After setting number served:", restaurant0.number_served)
restaurant0.increment_number_served(5)
print("After incrementing number served:", restaurant0.number_served)


#9.5
class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("User information:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Email:", self.email)

    def greet_user(self):
        print("Hello,", self.first_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Sergey", "Skiba", 40, "skiba.sergej1981gmail.com")
user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts:", user1.login_attempts)

user1.reset_login_attempts()
print("Login attempts after reset:", user1.login_attempts)

#0
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


#9.6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print("-", flavor)

ice_cream_stand = IceCreamStand("Sunny's Ice Cream",
                                "Ice Cream",
                                ["Vanilla", "Chocolate", "Strawberry"])
ice_cream_stand.show_flavors()


#9.7
class Admin(User):
    def __init__(self, first_name, last_name, age, email, privileges):
        super().__init__(first_name, last_name, age, email)
        self.privileges = privileges

    def show_privileges(self):
        print("privileges:")
        for privilege in self.privileges:
            print("-", privilege)

Admin = Admin("Sergey", "Skiba", 40, "skiba.sergej1981gmail.com", [
    "разрешено добавлять сообщения",
    "разрешено удалять пользователей",
    "разрешено банить пользователей"
])
Admin.show_privileges()


#9.7.1
class Admin(User):
    def __init__(self, first_name, last_name, age, email, privileges):
        super().__init__(first_name, last_name, age, email)
        self.privileges = privileges

    def show_privileges(self):
        print(f"{self.first_name} {self.last_name}'s privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
Admin = Admin("Sergey", "Skiba", 40, "skiba.sergej1981gmail.com", [
    "разрешено добавлять сообщения",
    "разрешено удалять пользователей",
    "разрешено банить пользователей"
])
Admin.describe_user()
Admin.show_privileges()


#9.8
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
Privileges = Privileges([
"разрешено добавлять сообщения",
"разрешено удалять пользователей",
"разрешено банить пользователей"
])
Privileges.show_privileges()


#9.9
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print("Battery upgraded to 85 kWh.")
        else:
            print("Battery is already at optimal size.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('Tesla', 'Model S', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


