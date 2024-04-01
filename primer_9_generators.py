def print_hello_1(name: str) -> None:
    print(f"Hello, {name}!")


def print_hello() -> None:
    name = input("Please enter your name: ")
    if name == "exit":
        return
    if not name:
        print("You must enter a name!")
        return print_hello()


def double_values_range(x: int):
    for i in range(x):
        print('Before print')
        yield i * 2
        print('After print')


def double_values_list(x: int) -> list[int]:
    result = []
    for i in range(x):
        result.append(i * 2)
    return result
    # the same functionality as above using list comprehension
    return [i * 2 for i in range(x)]


def run_double_using_for_loop():
    for i in double_values_range(5):
        print(i)


def run_doubles_using_while_loop():
    doubles = double_values_range(10)
    while True:
        try:
            print(next(doubles))
        except StopIteration:
            break


if __name__ == '__main__':
    run_double_using_for_loop()
