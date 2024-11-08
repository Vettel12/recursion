"""
В Темпограде объявлено о проведении соревнования. Уехать навсегда из города сможет тот, кто
напишет самое эффективное решение следующей задачи.
Опишем алгоритм построения последовательности бинарных строк. В первой строке записано
число 0. Для того, чтобы понять, что записано в следующей строке, нужно посмотреть на
предыдущую, и изменить каждый 0 на 01, и каждую 1 на 10. Таким образом, длина і-й строки в
2 раза больше, чем длина (і - 1)-й.
Приведем для ясности построение первых трех строк:
1.
2. 01
3. 0110
Ваша задача - по данным пик определить, какой символ будет находиться в п-й строке
-й позиции.
на k
Формат ввода
В первой строке записано п … число, не превосходящее 30. Во второй строке записано
число в диапазоне 1, 2(л 1)
Формат вывода
Выведите единственный символ 0 или 1 -- ответ на задачу.

Пример 1
Ввод
1
1
Вывод
0
Пример 2
Ввод
2
2
Вывод
1
Примечания
Индексация начинается с 1 (для п и для k).
"""

def solution(n, k):
    if n == 1:
        return '0'
    half_length = 2 ** (n - 2)
    if k <= half_length:
        return solution(n - 1, k)
    else:
        return '1' if solution(n - 1, k - half_length) == '0' else '0'


def main():
    try:
        n = int(input())
        if n > 30:
            raise ValueError("Invalid number")
        k = int(input())
        if k < 1 or k > 2**(n-1):
            raise ValueError("Invalid number")
        print(solution(n, k))
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()