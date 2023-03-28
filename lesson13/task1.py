print("Введите первое число")
a = float(input())
print("Введите второе число")
b = float(input())


def calculator(a, b, symbol):
    if symbol == "+":
        return a + b

    if symbol == "-":
        return a - b

    if symbol == "*":
        return a * b

    if symbol == "/":
        if b == 0:
            return "На 0 делить нельзя!"
        else:
            return a / b


print("Введите знак операции")
symbol = input()

print(eval(f'{a}{symbol}{b}'))
