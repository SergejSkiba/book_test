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
