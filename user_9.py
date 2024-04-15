#9.11
class User:
    def __init__(self, first_name: str, last_name: str, age: int, email: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.email: str = email

    def describe_user(self) -> None:
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self) -> None:
        print(f"Hello, {self.first_name}!")


class Privileges:
    def __init__(self, privileges: str | None = None) -> None:
        if privileges is None:
            self.privileges: str = []
        else:
            self.privileges: str = privileges

    def show_privileges(self):
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("No privileges assigned.")


class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, email: str) -> None:
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges([
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей",
])


admin_user = Admin("Sergey", "Skiba", 40, "skiba.sergej1981gmail.com")
admin_user.describe_user()
admin_user.privileges.show_privileges()