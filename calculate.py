def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль! Проверьте данные!"
    return x / y

def square(x):
    return x ** 2

def calculator():
    print("Простой калькулятор")
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Квадрат числа (^2)")

    while True:
        operation = input("Введите номер операции (1/2/3/4/5) или 'q' для выхода: ")

        if operation.lower() == 'q':
            print("Выход из калькулятора.")
            break

        if operation in ['1', '2', '3', '4', '5']:
            if operation == '5':
                try:
                    num = float(input("Введите число для вычисления квадрата: "))
                except ValueError:
                    print("Ошибка! Пожалуйста, введите числовое значение.")
                    continue
                print(f"Квадрат числа {num} = {square(num)}")
            else:
                try:
                    num1 = float(input("Введите первое число: "))
                    num2 = float(input("Введите второе число: "))
                except ValueError:
                    print("Ошибка! Пожалуйста, введите числовое значение.")
                    continue

                if operation == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif operation == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif operation == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif operation == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Неверный ввод! Пожалуйста, выберите операцию из списка.")

if __name__ == "__main__":
    calculator()
