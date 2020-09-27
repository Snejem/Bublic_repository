import random


class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def add(self, *args):
        self.value += sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if x == 0:
                print("Error, division by 0")
                return 0
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def pow(self, *args, power_index):
        i = len(args)
        while i > 0:
            if self.value == 0 and args[i] == 0:
                print("Error, 0^0 undefined")
                return 0
            self.value = self.value**args[i]
            i -= 1
        return self

    def root(self, *args, root_index):
        for i in args:
            if self.value == 0 and i == 0:
                print("Error, root of 0 power undefined")
                return 0
            self.value = self.value**1/i
        return self


def fun(x):
    return x[::-1]


if __name__ == '__main__':
    calculator = Calculator(random.randint(0, 100))
    print(calculator)
    print(calculator.add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))
    print(Calculator(100).value + 10)
    print(10 + Calculator(12).value)
    print(Calculator(123).value - Calculator(14).value)
    print(Calculator(14).value / Calculator(2).value)
