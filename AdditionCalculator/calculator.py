from addition import Addition


class Calculator:

    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        return Addition.add(num1, -num2)

    @classmethod
    def multiply(cls, num1, num2):
        total = 0
        for i in range(num2):
            total = Addition.add(total, num1)

        return total

    @classmethod
    def divide(cls, num1, num2):
        total = 0

        while Addition.add(num1, -num2) >= 0:
            num1 = Addition.add(num1, -num2)
            total = Addition.add(total, 1)

        return total
