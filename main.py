from math import *


def sin_series(x, terms):
    """
    Приближенное вычисление синуса с использованием ряда Тейлора.

    Параметры:
        x (float): Значение аргумента, для которого вычисляется синус.
        terms (int): Количество членов ряда для приближенного вычисления.

    Возвращает:
        float: Приближенное значение синуса для указанного x.
    """
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * ((x ** (2 * n + 1)) / (factorial(2 * n + 1)))
    return result


def chosin_series(x, terms):
    """
    Приближенное вычисление гиперболического косинуса (chosh x) с использованием ряда Тейлора.

    Параметры:
        x (float): Значение аргумента, для которого вычисляется гиперболический косинус.
        terms (int): Количество членов ряда для приближенного вычисления.

    Возвращает:
        float: Приближенное значение гиперболического косинуса для указанного x.
    """
    result = 0
    for n in range(terms):
        result += (x ** (2 * n)) / (factorial(2 * n))
    return result


def arctg_series(x, terms):
    """
    Приближенное вычисление арктангенса с использованием ряда Тейлора.

    Параметры:
        x (float): Значение аргумента, для которого вычисляется арктангенс.
        terms (int): Количество членов ряда для приближенного вычисления.

    Возвращает:
        float: Приближенное значение арктангенса для указанного x.
    """
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * ((x ** (2 * n + 1)) / (2 * n + 1))
    return result


def menu():
    """
    Выводит на экран текстовое меню с опциями для пользователя.
    """
    print("\n1. Вычислить синус x")
    print("2. Вычислить чосинус x")
    print("3. Вычислить арктангенс x")
    print("4. Выход из программы")


def input_float(prompt):
    """
    Безопасный ввод числа с проверкой на символы и буквы.

    Параметры:
        prompt (str): Текст запроса для ввода.

    Возвращает:
        float: Числовое значение, введенное пользователем.
    """
    while True:
        try:
            value = input(prompt).strip()
            if not value.replace(".", "", 1).replace("-", "", 1).isdigit():
                raise ValueError("Ввод содержит символы или буквы!")
            return float(value)
        except ValueError as e:
            print(f"Ошибка: {e}. Введите корректное число.")


def input_positive_int(prompt):
    """
    Безопасный ввод положительного целого числа.

    Параметры:
        prompt (str): Текст запроса для ввода.

    Возвращает:
        int: Положительное целое число, введенное пользователем.
    """
    while True:
        try:
            value = input(prompt).strip()
            if not value.isdigit() or int(value) <= 0:
                raise ValueError("Введите положительное целое число!")
            return int(value)
        except ValueError as e:
            print(f"Ошибка: {e}")


def main():
    while True:
        menu()
        choice = input("Выберите опцию (1-4): ").strip()

        if choice == "1":
            x = input_float("Введите значение x для sin x: ")
            terms = input_positive_int("Введите кол-во членов для приближенного вычисления: ")
            print(f"sin({x}) = {sin_series(x, terms)}")

        elif choice == "2":
            x = input_float("Введите значение x для chosin x: ")
            terms = input_positive_int("Введите кол-во членов для приближенного вычисления: ")
            print(f"chosin({x}) = {chosin_series(x, terms)}")

        elif choice == "3":
            x = input_float("Введите значение x для arctg x: ")
            terms = input_positive_int("Введите кол-во членов для приближенного вычисления: ")
            print(f"arctg({x}) = {arctg_series(x, terms)}")

        elif choice == "4":
            print("Выход.")
            break

        else:
            print("Ошибка, попробуйте еще раз!")


if __name__ == "__main__":
    main()
