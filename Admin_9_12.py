from User_9_12 import User

class Privileges:
    def __init__(self, privileges=["разрешено добавлять сообщения",
        "разрешено удалять пользователей",
        "разрешено банить пользователей"
    ]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
