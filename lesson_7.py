def task_1():
    message = input("what kind of car you would like to rent: ")
    print("Let me see if I can find you a " + message + ".")


def task_2():
    quantity = input("how many seats you would like to reserve in the restaurant: ")
    quantity = int(quantity)
    if quantity > 8:
        print("you'll have to wait")
    else:
        print("table is ready")


def task_3():
    number = input("Enter a number and I'll tell you if it's a multiple of 10 or not: ")
    number = int(number)
    if number % 10 == 0:
        print("\nThe number " + str(number) + " is even.")
    else:
        print("\nThe number " + str(number) + " is not divisible by 10.")


def task_4():
    prompt = "\nthis addendum is included in the order:"
    prompt += "\nEnter 'quit' to end the program. "
    pizza_toppings = ""
    while pizza_toppings != 'quit':
        pizza_toppings = input(prompt)
        print(pizza_toppings)


def task_5():
    age = input("how old you are?: ")
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print("ticket price is $" + str(price) + ".")


def task_6():
    active = True
    while active:
        age = input("How old are you? (Enter 'quit' to exit): ")
        if age == 'quit':
            break
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print("ticket price is $" + str(price) + ".")


def task_7():
    x = 2
    while x <= 5:
        print(x)
# Ctrl+C


def task_8():
    sandwich_orders = ['with_beef', 'with_chicken', 'with_pork', 'without_meat']
    finished_sandwiches = []
    while sandwich_orders:
        finished_sandwich = sandwich_orders.pop()
        print("cooked sandwich: " + finished_sandwich)
        finished_sandwiches.append(finished_sandwich)
    print("\nI made your sandwich: ")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich)


def task_9():
    sandwich_orders = ['with_beef', 'pastrami', 'with_chicken', 'pastrami', 'with_pork', 'without_meat', 'pastrami']
    finished_sandwiches = []
    print("Sorry, but we're all out of pastrami today.")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    while sandwich_orders:
        finished_sandwich = sandwich_orders.pop()
        print("Cooked sandwich: " + finished_sandwich)
        finished_sandwiches.append(finished_sandwich)
    print("\nI made your sandwich:")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich)


def task_10():
    dreams_vacation = {}
    polling_active = True
    while polling_active:
        name = input("\nWhat is your name? ")
        dream_vacation = input("Where you would they'd like to vacation? ")
        dreams_vacation[name] = dream_vacation
        repeat = input("Would you like to let another person respond? (yes/ no) ")
        if repeat == 'no':
            polling_active = False
    print("\n")
    for name, dream_vacation in dreams_vacation.items():
        print(name + " I'd like to spend my vacation " + dream_vacation + ".")


    if __name__ == '__main__':
        task_10()
