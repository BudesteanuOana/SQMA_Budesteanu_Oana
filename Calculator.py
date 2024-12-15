class Calculator:
   
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self,a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


if __name__ == "__main__":
    calc = Calculator()

    print("Addition: 3 + 5 =", calc.add(3, 5))
    print("Subtraction: 10 - 4 =", calc.subtract(10, 4))
    print("Multiplication: 7 * 6 =", calc.multiply(7, 6))

    try:
        print("Division: 8 / 2 =", calc.divide(8, 2))
        print("Division: 8 / 0 =", calc.divide(8, 0))
    except ValueError as e:
        print("Error:", e)

    try:
        print("Factorial: 5! =", calc.factorial(5))
        print("Factorial: -3! =", calc.factorial(-3))
    except ValueError as e:
        print("Error:", e)
