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


if __name__ == '__main__':
    task_11()
