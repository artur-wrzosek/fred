import math
from typing import Union


class Calc:
    @staticmethod
    def square_root(n: Union[int, float]) -> float:
        if n < 0:
            raise ValueError("Square root of a negative number does not exist")
        return math.sqrt(n)

    @staticmethod
    def power(base: Union[int, float], exponent: Union[int, float]) -> float:
        return math.pow(base, exponent)

    @staticmethod
    def log(n: float, base: float) -> float:
        if n <= 0 or base <= 0:
            raise ValueError("Number and base must be positive")
        if base == 1:
            raise ValueError("Base cannot be 1")
        return math.log(n, base)

    @staticmethod
    def nth_root(x: Union[int, float], root: int) -> float:
        if root == 0:
            raise ValueError("Root degree cannot be zero")

        if x < 0 and root % 2 ==0:
            raise ValueError("The even root of a negative number does not exist")

        if x < 0:
            return -math.pow(abs(x), 1/root)

        return math.pow(x, 1/root)

class CalcUI:
    options = {
        "1": "Square root",
        "2": "Power",
        "3": "Logarithm",
        "4": "N-th root",
        "0": "Exit",
    }

    @classmethod
    def print_menu(cls):
        print("Choose an option:")
        for i, option in cls.options.items():
            print(f"{i}. {option}")

    @staticmethod
    def get_number(message: str) -> float:
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Incorrect number! Please give a proper value")


def main():
    calc = Calc()
    ui = CalcUI()

    while True:
        ui.print_menu()
        try:
            choice = input()
            if choice == "1":
                number = ui.get_number("Enter a number: ")
                try:
                    result = calc.square_root(number)
                    print(f"Square root of {number} is equal to: {result}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "2":
                number = ui.get_number("Enter a number: ")
                exponent = ui.get_number("Enter an exponent: ")
                result = calc.power(number, exponent)
                print(f"Number {number} to the {exponent} exponent is equal to: {result}")

            elif choice == "3":
                number = ui.get_number("Enter a number: ")
                base = ui.get_number("Enter a logarithm base: ")
                try:
                    result = calc.log(number, base)
                    print(f"Logarithm of {number} with base {base} is equal to: {result}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "4":
                number = ui.get_number("Enter a number: ")
                degree = int(ui.get_number("Enter root degree: "))
                try:
                    result = calc.nth_root(number, degree)
                    print(f"{degree}th root of {number} is equal to: {result}")
                except ValueError as e:
                    print(f"Error: {e}")


            elif choice == "0":
                print("Thank you for using Calculator!")
                break

            else:
                print("Incorrect option. Choose again")
                input("Press enter to continue\n")

        except KeyboardInterrupt:
            print("Application terminated by user")
            break
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            input("Press enter to continue")

if __name__ == "__main__":
    main()