#9.11
class User:
    def __init__(self, first_name, last_name, age, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self) -> None:
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self) -> None:
        print(f"Hello, {self.first_name}!")


class Privileges:
    def __init__(self, privileges=None) -> None:
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("No privileges assigned.")


class Admin(User):
    def __init__(self, first_name, last_name, age, email) -> None:
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges([
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей",
])


admin_user = Admin("Sergey", "Skiba", 40, "skiba.sergej1981gmail.com")
admin_user.describe_user()
admin_user.privileges.show_privileges()
