"""
В конкурсе на самую быструю программу сортировки одинаковый результат получили к
человек. В призовом фонде имеется и монет различного достоинства. Нужно определить,
можно ли разделить их между победителями таким образом, чтобы каждый получил
одинаковую сумму.
Формат ввода
В первой строке задано k - количество победителей - целое число от 1 до 16. Во второй строке
задано п - количество монет - целое число, не превосходящее 16. Далее в строку через
пробел записано и чисел, каждое из которых не превосходит 10000.
Формат вывода
Нужно вывести True, если возможно разделить призовой фонд на равные части между
победителями, иначе - False.

Пример 1
Ввод
4
7
4 3 2 3 5 2 1
Вывод
True

Пример 2
Ввод
2
7
2 3 1 3 5 2 1
Вывод
False
"""

def solution(k, n, num):
    total = sum(num)
    if total % k != 0:
        return False
    target = total // k
    return can_partition(num, k, target)

def can_partition(num, k, target, current_sum=0, index=0):
    if k == 0:
        return True
    # Если текущая сумма достигла целевой, то продолжаем рекурсию
    if current_sum == target:
        return can_partition(num, k - 1, target, 0, 0)
    # Распределяем моменеты
    for i in range(index, len(num)):
        if current_sum + num[i] <= target:
            if can_partition(num, k, target, current_sum+num[i], i + 1):
                return True
    return False

def main():
    try:
        k = int(input())
        if k < 1 or k > 16:
            raise ValueError
        n = int(input())
        if n > 16:
            raise ValueError
        num = list(map(int, input().split()))
        for x in num:
            if x > 10000:
                raise ValueError
        print(solution(k, n, num))
    except ValueError:
        print("Число вне диапазона")

if __name__ == '__main__':
    main()