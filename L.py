"""
Тимофей пошел снять деньги в банкомат. Ему нужно т трешландийских долларов. В
банкомате в бесконечном количестве имеются монеты различных достоинств. Всего
различных достоинств 1. Монет каждого достоинства можно взять бесконечно много. Нужно
определить число способов, которыми Тимофей сможет набрать нужную сумму.
Формат ввода
В первой строке записано m - сумма, которую нужно набрать. Во второй строке п - количество
монет в банкомате. Оба числа не превосходят 300. Далее в строку записано п уникальных
чисел, каждое в диапазоне от 1 до 1000 - достоинства монет.
Формат вывода
Нужно вывести число способов, которым Тимофей сможет набрать нужную сумму.

Пример 1
Ввод
5
3
3 2 1
Вывод
5

Пример 2
Ввод
3
2
2 1
Вывод
2

Пример 3
Ввод
8
1
5
Вывод
0

Примечания
В первом примере возможны следующие варианты:
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 1 + 3
1 + 2 + 2
2 + 3
Во втором примере всего две возможности набрать в сумме 3:
1 + 2
1 + 1 + 1
В третьем примере есть всего один номинал, которым мы не можем набрать нужную сумму.
"""

def solution(m, n, number):
    def recursive_solution(current_sum, current_index):
        if current_sum == m:
            return 1
        if current_sum > m or current_index >= n:
            return 0
        return recursive_solution(current_sum+number[current_index], current_index) +\
            recursive_solution(current_sum, current_index+1)

    return recursive_solution(0, 0)

def main():
    try:
        m = int(input())
        if m > 300:
            raise ValueError
        n = int(input())
        number = list(map(int, input().split()))
        for i in range(n):
            if number[i] < 1 or number[i] > 1000:
                raise ValueError
        print(solution(m, n, number))
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()