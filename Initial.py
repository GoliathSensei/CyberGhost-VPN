class Calculator:
    def __init__(self):
        self.operations = {
            '+': self._add,
            '-': self._subtract,
            '*': self._multiply,
            '/': self._divide
        }

    def _add(self, a, b):
        return a + b

    def _subtract(self, a, b):
        return a - b

    def _multiply(self, a, b):
        return a * b

    def _divide(self, a, b):
        if b == 0:
            print("Error: Division by zero is not allowed!")
            return None
        return a / b

    def calculate(self, num1, operator, num2):
        operation = self.operations.get(operator)
        if not operation:
            valid_ops = ', '.join(self.operations.keys())
            print(f"Invalid operator! Please use: {valid_ops}")
            return None
        return operation(num1, num2)



def get_user_input():
    calculator = Calculator()

    print("Simple Calculator in Python")

    try:
        num1_input = input("Enter the first number: ")
        num1 = float(num1_input)

        operator = input("Enter an operator (+, -, *, /): ").strip()

        num2_input = input("Enter the second number: ")
        num2 = float(num2_input)

        result = calculator.calculate(num1, operator, num2)
        if result is not None:
            print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Please enter valid numbers!")
    except KeyboardInterrupt:
        print("\nCalculator terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    get_user_input()
