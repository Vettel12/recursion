"""
Другим важным математическим объектом является факториал.
Факториал вычислить циклически.
Пример 1
Ввод
3
Вывод
6

Пример 2
Ввод
1
Вывод
1
Решение может быть реализовано с помощью рекурсивной функции
"""

def solution(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for x in range(1, n+1):
            result *= x
        return result

def main():
    try:
        n = int(input())
        if n < 0 or n > 22:
            raise ValueError
        print(solution(n))
    except ValueError:
        print("Число вне диапазона")

if __name__ == '__main__':
    main()