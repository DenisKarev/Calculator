# from calc_input import menu_inp

def draw_menu_start():           # возможный выбор 012
    print(
        """Добро пожаловать в not so friendly Калькулятор !
Выберите с какими числами будете работать:
    1. Вещественный
    2. Комплексные

    0. Выход""")
    return


def draw_menu_real():           # возможный выбор 012345678
    print(
        """Меню работы с Вещественными числами:
    1. Cумма двух чисел
    2. Разность двух чисел
    3. Умножение двух чисел
    -> Деление чисел
       4. Деление двух чисел
       5. Целочисленное деление двух чисел
       6. Деление двух чисел с остатком
    7. Возведение числа в спепень числа ))
    8. Квадратный корень числа

    0. Предыдущее меню"""
    )
    return


def draw_menu_real_divs():          # это остатки от мыслей по разделению Деление чисел (*см выше) в отдельное меню
    return


def draw_menu_complex():                       # возможный выбор 0123456
    print("""Меню работы с Комплексными числами:
    1. Cумма двух чисел
    2. Разность двух чисел
    3. Умножение двух чисел
    4. Деление двух чисел
    5. Возведение числа в спепень числа ))
    6. Квадратный корень числа

    0. Предыдущее меню""")
    return

def draw_result(val: str):          # что передаем на вывод? и отдельно ли для комплексных? 
    print(f"""    Результат выбранной операции: {val}""")       # округляем? (не помню как %)))
    return                           # ars # Что модули возвращают то и предаем на вывод)))

draw_result('11')                   # тестирование вывода