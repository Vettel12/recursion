"""
Другим важным математическим объектом является факториал.
Факториал - это произведение чисел от 1 до n.
На Пресной воде существует своя система кодирования - Кондратьева. Число в этой системе
кодируется с помощью значения факториала. Дочь Кондратия, Евлампия, использует эту систему
для шифрования пароля iPhone. Помогите Евлампии зашифровать пароль. Вам нужно
написать рекурсивную реализацию функции, которая вычисляет факториал заданного числа.
Формат ввода
Входными данными является положительное целое число в диапазоне от 0 до 20.
Формат вывода
Вам необходимо вывести факториал заданного числа.

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
    return n*solution(n-1)

def main():
    try:
        n = int(input())
        if n < 0 or n > 20:
            raise ValueError
        print(solution(n))
    except ValueError:
        print("Число вне диапазона")

if __name__ == '__main__':
    main()