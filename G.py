"""
Кондратий решил заняться изучением английского языка и организовал соревнование. Билет на
тараканьи бега получит тот, кто напишет самую быструю функцию, рекурсивно выводящую
английский алфавит до заданной буквы включительно.
Формат ввода
На входе указывается строчная буква английского алфавита.
Формат вывода
Вам необходимо напечатать ответ - алфавит от начала до указанной буквы - в строке, разделенной пробелом.
Пример 1
Ввод
z
Вывод
a, b, c, d, e, g, h, i, j, k...

Пример 2
Ввод
c
Выход
a b c
"""

def solution(letter):
    if letter == 'a':
        print ('a', end='')
    else:
        solution(chr(ord(letter) - 1))
        print(' ' + letter, end='') 

def main():
    letter = input()
    solution(letter)

if __name__ == '__main__':
    main()