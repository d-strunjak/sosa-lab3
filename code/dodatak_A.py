import getpass
import hashlib
from math import nan


class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        if self.b==0: return nan
        return self.a / self.b


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    digest = hashlib.sha256(password.encode()).hexdigest()
    if user != "root" or digest != "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3":
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        a = float(input("A = "))
        b = float(input("B = "))
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())

