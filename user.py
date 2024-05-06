class User:
    def __init__(self, userid, username, password):
        self._userid = userid
        self._username = username
        self._password = password

    @property
    def userid(self):
        return int(self._userid)

    @userid.setter
    def userid(self, userid):
        if not userid:
            raise ValueError("User ID is required")
        if len(str(userid)) != 8:
            raise ValueError("User ID must be 8 characters long")
        try:
            userid = int(userid)
        except ValueError:
            raise ValueError("User ID must be an integer")
        self._userid = userid

    @property
    def username(self):
        return str(self._username)

    @username.setter
    def username(self, username):
        if not username:
            raise ValueError("Username is required")
        self._username = username

    @property
    def password(self):
        return str(self._password)

    @password.setter
    def password(self, password):
        if not password:
            raise ValueError("Password is required")
        self._password = password

    def get_user(self):
        return self.username

    def show(self):
        return "\n".join([
            f"User ID: {self.userid}",
            f"Username: {self.username}",
            f"Password: {self.password}"
        ])

    def __str__(self):
        return self.show()


if __name__ == "__main__":
    print("Start Tests")
    user = User(userid=12345678, username="kat", password="katherine")
    print(user)
    assert (
            str(user)
            == "User ID: 12345678\nUsername: kat\nPassword: katherine"
    ), "__str__ not the same"

    assert (
            user.show()
            == "User ID: 12345678\nUsername: kat\nPassword: katherine"
    ), "show not the same"

    print(user.username)
    user.username = "kat"
    print(user.username)
    assert user.username == "kat", "just a getter and setter"

    try:
        user.userid = 12345
    except ValueError:
        pass
    except:
        raise

    print("End Tests")
