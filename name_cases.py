def task_1():
    name = "sergej"
    print("Hello, " + name.title() + " would you like to learn some Python today?")
    print(name.lower())
    print(name.upper())
    print(name.title())


def task_2():
    message = '"It takes discipline, willpower and character to succeed."'
    author = "Sergej Skiba once said, "
    print(author + message)
    famous_persone = "Albert Einstein - "
    message = '"Strive not for success, but for the value it provides"'
    print(famous_persone + message)


def task_3():
    name = "  Sergej Skiba  "
    print(name.strip() + "\n\tdiscipline\n\twillpower\n\tcharacter")
    print(name.rstrip())
    print(name.lstrip())


def task_4():
    print(1 + 7)
    print(10 - 2)
    print(2 * 4)
    print(64 / 8)
    number = 9
    print(number)


def task_5():
    import this


def task_6():
    friends = ['petr', 'sergej', 'iliya']
    print(friends[0])
    print(friends[1])
    print(friends[2])
    print("Hello my friend, " + friends[0].title())
    print("Hello my friend, " + friends[1].title())
    print("Hello my friend, " + friends[2].title())

def task_7():
    cars = ['Mercedes', 'Hyundai', 'Porsche', 'Bentley', 'bmw', 'audi', 'toyota', 'subaru']
    print("I like cars: " + cars[2] + " and " + cars[3] + ", " + "but I'm driving a " + cars[1] + "!")
    guests = ["vera", "nina", "lena"]
    print('Hi,' + guests[-3].title() + ' come to my place for lunch.')
    print('Hi,' + guests[-2].title() + ' come to my place for lunch.')
    print('Hi,' + guests[-1].title() + ' come to my place for lunch.')
    there_will_be_no_guest = "vera"
    guests.remove(there_will_be_no_guest)
    print(guests)
    print(there_will_be_no_guest.title() + " will not come.")
    guests.insert(0, "vika")
    print('Hi,' + guests[0].title() + ' come to my place for lunch.')
    print('Hi,' + guests[1].title() + ' come to my place for lunch.')
    print('Hi,' + guests[2].title() + ' come to my place for lunch.')
    guests.insert(0, "ola")
    guests.insert(2, "sofija")
    guests.append("liza")
    print(len(guests))
    print('Hi,' + guests[0].title() + ' come to my place for lunch.')
    print('Hi,' + guests[1].title() + ' come to my place for lunch.')
    print('Hi,' + guests[2].title() + ' come to my place for lunch.')
    print('Hi,' + guests[3].title() + ' come to my place for lunch.')
    print('Hi,' + guests[4].title() + ' come to my place for lunch.')
    print('Hi,' + guests[5].title() + ' come to my place for lunch.')
    print(guests)
    popper_guest = guests.pop()
    print("I regret cancelling the invitation " + popper_guest.title() + ".")
    popper_guest = guests.pop()
    print("I regret cancelling the invitation " + popper_guest.title() + ".")
    popper_guest = guests.pop()
    print("I regret cancelling the invitation " + popper_guest.title() + ".")
    popper_guest = guests.pop()
    print("I regret cancelling the invitation " + popper_guest.title() + ".")
    print(guests[0].title() + " i confirm that the earlier invitation still stands.")
    print(guests[1].title() + " i confirm that the earlier invitation still stands.")
    del guests[:]
    print(guests)


def task_8():
    countries = ['thailand', 'spain', 'portugal', 'italy', 'australia']
    print(countries)
    countries.sort()
    print(countries)
    countries.reverse()
    print(countries)
    countries.reverse()
    print(countries)
    print(len(countries))


def task_9():
    pizzas = ['with_meat', 'with_cheese', 'vegetarian']
    for pizza in pizzas:
        print(pizza + " - I like pepperoni pizza")
    print("\n".join(pizzas) + " - I\n\treally love\n\tpizza!")
    animals = ['swan', 'pike', 'crayfish']
    for animal in animals:
        print(animal + ", A dog would make a great pet")
    print("\nAny of these animals would make a great pet!")


def task_10():
    for value in range(1, 21):
        print(value)
    numbers = list(range(1, 1_000_001))
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))
    odd_numbers = list(range(1, 21, 2))
    for number in odd_numbers:
        print(number)
    every_third_day = list(range(3, 31, 3))
    for third in every_third_day:
        print(third)
    cubes = []
    for value in range(1, 11):
        cubes.append(value**3)
    print(cubes)
    cubes = [value**3 for value in range(1, 11)]
    print(cubes)


def task_11():
    cars = ['Mercedes', 'Hyundai', 'Porsche', 'Bentley', 'bmw', 'audi', 'toyota', 'subaru']
    print("The first three items in the list are:")
    for car in cars[:3]:
        print(car)
    print("\n""The first three items in the list are:")
    for car in cars[2:5]:
        print(car)
    print("\n""The first three items in the list are:")
    for car in cars[-3:]:
        print(car)
    my_pizzas = ['with_meat', 'with_cheese', 'vegetarian']
    friend_pizzas = my_pizzas[:]
    my_pizzas.append('Mexican')
    friend_pizzas.append('barbecue')
    print("My favorite pizzas are:")
    for my_pizza in my_pizzas:
        print(my_pizza)
    print("My friend’s favorite pizzas are:")
    for friend_pizza in friend_pizzas:
        print(friend_pizza)
    print("My favorite pizzas are:")
    print(my_pizzas)
    print("My friend’s favorite pizzas are:")
    print(friend_pizzas)
    menu = ('soup', 'pasta', 'salad', 'tea', 'dessert')
    for menu1 in menu:
        print(menu1)
        menu = ('roast', 'fish', 'salad', 'tea', 'dessert')
    print("\nModified menu:")
    for menu1 in menu:
        print(menu1)


def task_12():
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


if __name__ == '__main__':
    def task():