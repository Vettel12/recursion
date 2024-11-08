"""
По дороге в Удотинск ребятам встретилось поле, на котором местные жители выращивали
подорожники. Поле разделено на одинаковые квадраты. Размер квадратов вычислялся по
алгоритму, который использовал Овощеслав для схожей задачи.
Тимофей рассказал друзьям, что, если размер участка равен а на b, можно найти такие целые
числа х и у, что они, будучи умноженными на а и b, в сумме дадут наибольший общий
делитель а и b.
Помогите ребятам по двум числам найти их НОД и коэффициенты его разложения в линейную
комбинацию через эти числа.
Формат ввода
В первой строке записана ширина участка, во второй - длина. Оба числа не превосходят
10000.
Формат вывода
Выведите в строку через пробел 3 числа: коэффициент для а, коэффициент для b в
разложении НОД в линейную комбинацию через а и b, и сам НОД.

Пример 1
Ввод
8
12
Вывод
-1 1 4


Пример 2
Ввод
15
5
Вывод
0 1 5

Пример 3
Ввод
2
5
Вывод
-2 1 1

Примечания
Если возможных комбинаций несколько, то выведите любую, где коэффициенты умещаются в
32-битный знаковый тип.
"""

def solution(a, b):
    if a == 0:
        return 0, 1, b
    x, y, d = solution(b % a, a)
    return y - (b // a) * x, x, d

def main():
    try:
        a = int(input())
        if a > 10000:
            raise ValueError
        b = int(input())
        if b > 10000:
            raise ValueError
        a, b, d = solution(a, b)
        print(a, b, d)
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()