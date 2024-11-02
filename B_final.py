"""
Поиск в сломанном массиве
Алла ошиблась со структурой данных. Она решила хранить массив в кольцевом буфере.
Проблема в том, что массив был отсортирован. И в нем можно было искать элемент за
логарифмическое время. Алла скопировала данные из кольцевого буфера а обычный массив.
Но он больше не является отсортированным. Тем не менее нужно обеспечить возможность
находить в нем элемент за O(logn).

Формат ввода
В первой строке записано число n - длина массива.
Во второй строке записано положительное число k - искомый элемент.
n и k не превосходят 1000. Далее в строку через пробел записаны n положительных чисел,
каждое из которых не превосходит 1000.

Формат вывода
Выведите индекс искомого элемента в массиве, если он найден. Иначе выведите -1.

Ввод:
8
3
1 2 3 5 6 7 9 0

Вывод:
2

Ввод:
7
5
0 2 6 7 8 9 10

Вывод:
-1

Ввод:
1
1
1

Вывод:
0
"""

def solution(n, k, array, left = 0, right = None):
    if right is None:
        right = n
    if left > right:
        return -1
    middle = (left+right)//2
    if array[middle] == k:
        return middle
    #Ищем в левом подмассиве
    if array[left] <= array[middle]:
        if array[left] <= k and k < array[middle]:
            return solution(n, k, array, left, middle-1)
        else:
            return solution(n, k, array, middle+1, right)
    #Ищем в правом подмассиве
    else:
        if array[middle] < k and k <= array[right]:
            return solution(n, k, array, middle+1, right)
        else:
            return solution(n, k, array, left, middle-1)
    

def main():
    try:
        n = int(input())
        if n > 10000:
            raise ValueError
        k = int(input())
        if k > 10000:
            raise ValueError
        array = list(map(int, input().split()))
        for i in range(len(array)):
            if array[i] > 10000:
                raise ValueError
        print(solution(n, k, array))
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()