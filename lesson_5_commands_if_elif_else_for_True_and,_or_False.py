car = 'bmw'
print(car == 'bmw')
print(car == 'audi')
car = 'Audi'
print(car.lower() == 'audi')
age_0 = 18
age_1 = 21
print(age_0 >= age_1)
print(age_0 <= age_1)
print(age_0 <= 18 and age_1 >= 22)
print(age_0 <= 18 or age_1 >= 22)
cars = ['Subaru', 'Hyundai', 'Bmw', 'Audi', 'Toyota']
for car in cars:
    if car.lower() == 'audi':
        print(car.upper())
    else:
        print(car.title())
alien_color = 'green'
if alien_color == 'green':
    print("the player scored 5 points")
alien_color = 'yellow'
if alien_color == 'green':
    print("the player scored 5 points")
else:
    print("the player scored 10 points")
alien_color = 'red'
if alien_color == 'green':
    print("the player scored 5 points")
elif alien_color == 'yellow':
    print("the player scored 10 points")
else:
    print("the player scored 15 points")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age > 60:
    price = 7
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")
years = 42
if years < 2:
    life_stage = "infant"
elif years < 4:
    life_stage = "baby"
elif years < 13:
    life_stage = "child"
elif years < 20:
    life_stage = "teenager"
elif years < 65:
    life_stage = "adult"
else:
    life_stage = "elderly person"
print("life stage: " + life_stage)
favorite_fruit = ['mango', 'pear', 'kiwi']
if 'apple' in favorite_fruit:
    print("You really like apple!")
if 'pear' in favorite_fruit:
    print("You really like pear!")
if 'cherry' in favorite_fruit:
    print("You really like cherry!")
if 'plum' in favorite_fruit:
    print("You really like plum!")
if 'mango' in favorite_fruit:
    print("You really like mango!")
usernames = ['administrator', 'mikhail', 'alexander', 'vasily', 'alexei']
for username in usernames:
    if username == 'administrator':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again")
hello_admins = []
if hello_admins:
    for hello_admin in hello_admins:
        if hello_admin == 'admin':
            print("Hello {}".format(hello_admin) + ", would you like to see a status report?")
        else:
            print(f"Hello {hello_admin}, thank you for logging in again")
else:
    print("We need to find some users!")
current_users = ['sergej', 'mikhail', 'alexander', 'vasily', 'alexei']
new_users = ['sergej', 'lena', 'toma', 'ira', 'alexei']
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print(f"The username {new_user} is already in use. Please choose another name.")
    else:
        print(f"The user name {new_user} is available.")
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        ordinal = '1st'
    elif number == 2:
        ordinal = '2nd'
    elif number == 3:
        ordinal = '3rd'
    else:
        ordinal = f'{number}th'
    print(ordinal)
