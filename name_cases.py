name = "sergej"
print("Hello, " + name.title() + " would you like to learn some Python today?")
print(name.lower())
print(name.upper())
print(name.title())
message = '"It takes discipline, willpower and character to succeed."'
author = "Sergej Skiba once said, "
print(author + message)
famous_persone = "Albert Einstein - "
message = '"Strive not for success, but for the value it provides"'
print(famous_persone + message)
name = "  Sergej Skiba  "
print(name.strip() + "\n\tdiscipline\n\twillpower\n\tcharacter")
print(name.rstrip())
print(name.lstrip())
print(1 + 7)
print(10 - 2)
print(2 * 4)
print(64 / 8)
number = 9
print(number)
import this
friends = ['petr', 'sergej', 'iliya']
print(friends[0])
print(friends[1])
print(friends[2])
print("Hello my friend, " + friends[0].title())
print("Hello my friend, " + friends[1].title())
print("Hello my friend, " + friends[2].title())
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
countries = ['thailand', 'spain', 'portugal', 'italy', 'australia']
print(countries)
countries.sort()
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
print(len(countries))
pizzas = ['with_meat', 'with_cheese', 'vegetarian']
for pizza in pizzas:
    print(pizza + " - I like pepperoni pizza")
print("\n".join(pizzas) + " - I\n\treally love\n\tpizza!")
animals = ['swan', 'pike', 'crayfish']
for animal in animals:
    print(animal + ", A dog would make a great pet")
print("\nAny of these animals would make a great pet!")
