"""
У одного жителя деревни Упыревка очень старый компьютер. На экран он может
выводить только одну цифру, причем последнюю из тех, что выводится в
стандартный поток вывода. Помогите жителю Упыревки понять, что должно быть
выведено на экран, когда он запустит программу для вычисления n - ого числа Фибоначчи.

Формат ввода
На вход подается n - целое число в диапазоне от 0 до 10000

Формат вывода
Нужно вывести одну цифру, последнюю в числе, равному n - ому числу Фибоначчи

Ввод:
7

Вывод:
1
Ввод:
2
Вывод:
2

def solution(n):
    if n == 0 or n == 1:
        return 1
    F1 = 1
    F2 = 1
    num = n % 60
    for x in range(2, num):
        F2 = F1 + F2
        F1 = F2 - F1
    return str(F2)[-1]

"""

def solution(n):
    if n == 0 or n == 1:
        return 1
    last_digit = [1, 1]
    for x in range(2, 60):
        last_digit.append((last_digit[-1] + last_digit[-2]) % 10)
    return last_digit[n % 60 - 1]

def main():
    try:
        n = int(input())
        if n < 0 or n > 10000:
            raise ValueError
        print(solution(n))
    except ValueError:
        print("Число вне диапазона")

if __name__ == '__main__':
    main()