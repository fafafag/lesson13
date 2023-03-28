def decorator(func):
    def wrapper():
        name = func()
        print(f"Привет, {name}!")
    return wrapper

@decorator
def get_name():
    print("Введите имя:")
    name = input()
    return name

get_name()
