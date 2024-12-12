def cube(number):
    """Вычисляет куб (третью степень) заданного числа."""
    return number ** 3

# Основной код
while True:
    try:
        # Получаем число от пользователя
        user_input = input("Введите число для вычисления куба (или 'q' для выхода): ")
        
        # Проверяем, хочет ли пользователь выйти
        if user_input.lower() == 'q':
            print("Программа завершена.")
            break
            
        # Преобразуем ввод в число и вычисляем куб
        number = float(user_input)
        result = cube(number)
        
        # Выводим результат
        print(f"Куб числа {number} равен: {result}")
        
        # Дополнительно показываем промежуточные вычисления
        print(f"Промежуточные шаги:")
        print(f"{number} × {number} = {number * number}")
        print(f"{number * number} × {number} = {result}")
        
    except ValueError:
        print("Ошибка! Пожалуйста, введите корректное число.")
        continue