"""
В Долинске объявлен конкурс. Вам нужно написать самую быструю реализацию функции, которая
генерирует все правильные последовательности скобок длиной n.
Существует только один тип скобок: ( )
Формат ввода
В качестве входных данных функция принимает целое число от 0 до 10.
Формат вывода
Функция должна вывести все возможные последовательности скобок в указанном
лексикографическом порядке.
длина в

Пример 1
Ввод
3
Вывод
((()))
(()())
(())()
()(())
()()()

Пример 2
Ввод
2
Выход
(())
()()
Примечания
Строка A лексикографически меньше другой строки B, если она является точной копией
префикс B или, если есть такой индекс i, i < A], i < B , что A[i] < B[i].
"""

def solution(n):
    result = []
    generate_parentheses('', 0, 0, n, result)
    return result

def generate_parentheses(current, open_count, close_count, n, result):
    # Если длина текущей строки равна 2n, добавляем её в результат
    if len(current) == 2 * n:
        result.append(current)
        return
    if open_count < n:
        generate_parentheses(current + '(', open_count+1, close_count, n, result)
    if close_count < open_count:
        generate_parentheses(current + ')', open_count, close_count+1, n, result)

def main():
    try:
        n = int(input())
        if n < 0 or n > 10:
            raise ValueError
        for x in solution(n):
            print(x)
    except ValueError:
        print("Число вне диапазона")

if __name__ == '__main__':
    main()