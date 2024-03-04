def task_1():
    man = {'first_name': 'kesha', 'last_name': 'smaktunovskij', 'age': 50, 'city': 'minsk'}
    for key, value in man.items():
        print(f"{key.title()}: {value}")


def task_2():
    keys = {1: 'sergej', 2: 'mikhail', 3: 'alexander', 4: 'vasily', 5: 'alexei'}
    for number, people in keys.items():
        print(f"{number}: {people}")


def task_3():
    glossary = {
        'Variable': 'An object for storing data whose value can change during program execution.',
        'Cycle': 'A control structure that allows a set of instructions to be executed repeatedly.',
        'Function': 'A block of code that is organized to perform one specific task and can be called by name.',
        'Dictionary': 'A data structure in Python that represents a set of key-value pairs.',
        'Conditional Expression': 'An expression that allows an algorithm to make decisions based on the fulfillment or non-fulfillment of a specified condition.'
    }
    for term, definition in glossary.items():
        print(f"{term}:\n\t{definition}\n")
    glossary['module'] = 'A file containing Python definitions and instructions for use in other Python programs.'
    glossary['exception'] = 'An event that occurs during program execution that interrupts the normal flow of instructions.'
    glossary['Iterator'] = 'An object that allows the programmer to loop through the elements of a collection (such as a list or tuple).'
    glossary['Decorator'] = 'A special form of function that allows you to change the behavior of functions or methods.'
    glossary['Generator'] = 'A function that returns an iterator. It looks like a normal function, but uses a yield clause instead of return to return data.'
    for term, definition in glossary.items():
        print(f"{term}:\n\t{definition}\n")


def task_5():
    dictionary = {'Nile': 'Egypt', 'Amazon': 'Brazil', 'Sena': 'France'}
    for river, country in dictionary.items():
        print(f"The {river} runs through {country}.")
    for river in dictionary.keys():
        print(river)
    for country in dictionary.values():
        print(country)


def task_6():
    people_to_test = {'sergej', 'mikhail', 'alexander', 'vasily', 'alexei'}
    people_who_have_been_tested = {'sergej', 'alexei'}
    for person in people_to_test:
        if person in people_who_have_been_tested:
            print(f"Thank you, {person}, for participating in the test.")
        else:
            print(f"{person}, please consider participating in the test.")


def task_7():
    man = {'first_name': 'kesha', 'last_name': 'smaktunovskij', 'age': 50, 'city': 'minsk'}
    character = {'first_name': 'kolobok', 'last_name': 'kolobkovich', 'age': 70, 'city': 'tale'}
    actor = {'first_name': 'jean_claude', 'last_name': 'vandam', 'age': 63, 'city': 'usa'}
    people = [man, character, actor]
    for person in people:
        print("human_info:")
        for key, value in person.items():
            print(f"{key.title()}: {value}")
        print("\n")


def task_8():
    animals = {'animal_specie': 'wolf', 'color': 'gray', 'owner': 'no_owner'}
    pet = {'animal_specie': 'parrot', 'color': 'green', 'owner': 'sergey'}
    domestic_animal = {'animal_specie': 'cow', 'color': 'black_and_white', 'owner': 'grandmother'}
    pets = [animals, pet, domestic_animal]
    for animal in pets:
        print("info:")
        for key, value in animal.items():
            print(f"{key}: {value}")
        print("\n")


def task_10():
    keys = {
        'sergej': [7, 13],
        'mikhail': [1, 4, 9],
        'alexander': [3, 6],
        'vasily': [5, 10, 15],
        'alexei': [2, 8],
    }
    for person, favorite_numbers in keys.items():
        print(f"{person.title()}'s favorite numbers are:")
        for number in favorite_numbers:
            print(f"\t- {number}")
        print()


def task_11():
    cities = {
        'novopolotsk': {'country': 'belarus', 'population': '110_000 people ', 'fact': 'petrograd_city'},
        'vilnius': {'country': 'lietuva', 'population': '600_000 people', 'fact': 'green_city'},
        'bangkok': {'country': 'thailand', 'population': '8_280_000 people', 'fact': 'muaythai_city'},
    }
    for city_name, city_info in cities.items():
        print(f"{city_name=}")
        for town, fact in city_info.items():
            print(f"{town}: {fact}")
        print("")


def task_12():
    pets = {
        'animals': {'animal_specie': 'wolf', 'color': 'gray', 'owner': 'no_owner'},
        'pet': {'animal_specie': 'parrot', 'color': 'green', 'owner': 'sergey'},
        'domestic_animal': {'animal_specie': 'cow', 'color': 'black_and_white', 'owner': 'grandmother'},
    }
    for pet_name, pet_info in pets.items():
        print(f"pet: {pet_name}")
        for key, value in pets.items():
            print(f"{key}: {value}")
        print("\n")
