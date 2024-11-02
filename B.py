"""
Функция из прошлого задания работала слишком долго. Нужно модифицировать ее
таким образом, чтобы одни и те же значения повторно не вычислялись.

Формат ввода
На вход подается число n.

Формат вывода
Напечатайте n-ное число Фибоначчи
"""

def solution(n):
    capacity = {0: 1, 1: 1}
    for x in range(2, n+1):
        if x not in capacity:
            capacity[x] = capacity[x-1] + capacity[x-2]
    return capacity[n]

def main():
    try:
        n = int(input())
        if n < 0 or n > 30:
            raise ValueError
        print(solution(n))
    except ValueError:
        print("Число вне диапазона")

if __name__ == '__main__':
    main()