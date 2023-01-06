from load_config import get_value


class AppStart:
    username = None

    def __init__(self):
        u = get_value('USERNAME')
        if not u:
            raise ValueError("unable to find username")

        self.username = u

    def connect(self):
        print(f"connecting with {self.username}")

        return self.username


if __name__ == "__main__":
    obj = AppStart()
    print(obj.connect())
