"""
У многих жителей Трешландии на компьютере осталось совсем мало свободного места.
Но они тоже хотят иметь возможность вычислять, сколько животных могут завести.
Нужно оптимизировать решение задачи про вычисление чисел Фибоначчи.
Объем дополнительной памяти должен быть O(1).

Формат ввода
На вход подается n - целое число в диапазоне от 0 до 30.
Формат вывода
Нужно вывести значение n - ого числа Фибоначчи.

Примечания
Решение должно работать за O(n) и использовать O(1) дополнительной памяти.

"""

def solution(n):
    if n == 0 or n == 1:
        return 1
    F1 = 1
    F2 = 1
    for x in range(2, n+1):
        F2 = F1 + F2
        F1 = F2 - F1
    return F2

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