"""
Формат ввода
В первой строке записана ширина участка, во второй - длина. Оба числа не превосходят 10000.
Формат вывода
Нужно вывести максимально возможный размер квадратных участков, на который можно
разделить территорию.

Пример 1
Ввод
15
18
Вывод
3

Пример 2
Ввод
2
1
Вывод
1
"""

def solution(a, b):
    if a > b and a % b == 0:
        return b
    elif a < b and b % a == 0:
        return a
    else:
        if a > b:
            return solution(b, a % b)
        else:
            return solution(a, b % a)
        

def main():
    try:
        a = int(input())
        if a > 10000:
            raise ValueError
        b = int(input())
        if b > 10000:
            raise ValueError
        print(solution(a, b))
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()