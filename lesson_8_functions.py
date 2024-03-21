# 1
def display_message(message):
    print("A post on how I spent my weekend: " + message + ".")
display_message("admirably")


# 2
def favorite_book(namebook):
    print("One of my favorite books: " + namebook.title() + "!")
favorite_book("alice in wonderland.")


# 3,4
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text to be printed is: '{text}'.")
make_shirt('M', 'boxing and python!')
make_shirt('L', 'I love Python.')
make_shirt('S', 'Study.')


# 5
def describe_city(city, country="Belarus"):
    print(f"{city} is in {country}.")
describe_city("Minsk")
describe_city("Novopolotsk")
describe_city("Vilnius", "Lietuva")


# 6
def city_country(city, country):
    print(f"{city}, {country}")
    return f"{city}, {country}"
city_country("Santiago", "Chile")
city_country("Warsawa", "Poland")
city_country("Vilnius", "Lietuva")


# 7
def make_album(artist, album_title):
    return {artist:album_title}
print(make_album('The Beatles', 'Abbey Road'))
print(make_album('Pink Floyd', 'The Dark Side of the Moon'))
print(make_album('Adele', '21'))


# 8
def make_album(artist, album_title):
    return {artist: album_title}
albums = []
while True:
    print("\nPlease enter the artist name and album title:")
    print("(enter 'quit' at any time to stop)")
    artist = input("Artist: ")
    if artist == 'quit':
        break
    album_title = input("Album title: ")
    if album_title == 'quit':
        break
    album = make_album(artist, album_title)
    albums.append(album)
print(albums)


# 9
def show_magicians(magicians):
    for magician in magicians:
        msg = "Hello, " + magician.title() + "!"
        print(msg)
magicians = ['nif_nif', 'nuf_nuf', 'naf_naf']
show_magicians(magicians)


# 10
def make_great_gpt(magicians):
    for i in range(len(magicians)):
        magicians[i] = "Great " + magicians[i]
    return magicians
magicians = ['nif_nif', 'nuf_nuf', 'naf_naf']
make_great_gpt(magicians)
show_magicians(magicians)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# 11
def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append("Great " + magician)
    return great_magicians
magicians = ['nif_nif', 'nuf_nuf', 'naf_naf']
great_magicians = make_great(magicians)
print("Original magicians:")
show_magicians(magicians)
print("\nGreat magicians:")
show_magicians(great_magicians)


# 12
def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
make_sandwich('ham', 'cheese', 'tomato')
make_sandwich('turkey', 'avocado')
make_sandwich('peanut butter', 'jelly')


# 13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                                 location='princeton',
                                 field='physics')
print(user_profile)


# 14
def cars(manufacturer, model, **user_info):
    cars_info = {}
    cars_info['manufacturer'] = manufacturer
    cars_info['model'] = model
    for key, value in user_info.items():
        cars_info[key] = value
    return cars_info
car = cars('subaru', 'outback', color='blue', tow_package=True)
print(car)


# 15



