# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-92.
Решение на языке Python 3.
Автор: Юрий Кондрашов, 2018
-------------------------------------------------
92) В физической лаборатории проводится долговременный эксперимент 
по изучению гравитационного поля Земли. По каналу связи каждую минуту 
в лабораторию передаётся положительное целое число – текущее показание 
прибора «Сигма 2015». Количество передаваемых чисел в серии известно 
и не превышает 10 000. Все числа не превышают 1000. Временем, в течение 
которого происходит передача, можно пренебречь.
Необходимо вычислить «бета-значение» серии показаний прибора – минимальное 
чётное произведение двух показаний, между моментами передачи которых прошло 
не менее 6 минут. Если получить такое произведение не удаётся, ответ 
считается равным –1.
Задача А. Напишите программу для решения поставленной задачи, в которой 
входные данные будут запоминаться в массиве, после чего будут проверены 
все возможные пары элементов. Максимальная оценка за выполнение задания 
А – 2 балла.
Задача Б. Напишите программу для решения поставленной задачи, которая 
будет эффективна как по времени, так и по памяти (или хотя бы по одной 
из этих характеристик).
Входные данные представлены следующим образом. В первой строке задаётся 
число N – общее количество показаний прибора. Гарантируется, что N > 6. 
В каждой из следующих N строк задаётся одно положительное целое число – 
очередное показание прибора.
Пример входных данных:
11
12
45
5
3
17
23
21
20
19
18
17
Программа должна вывести одно число – описанное в условии произведение 
либо –1, если получить такое произведение не удаётся.
Пример выходных данных для приведённого выше примера входных данных:
54
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/92.in")

buf = []  # место для хранения значений
k = 6  # отступ от текущего значения
mp = 1002 * 1002  # минимальное значение в последовательности
cur = 0  # граница кольцевой очереди
min_a = mp  # для минимальных значений
min_e = mp  # для минимальных чётных значений
num = int(input())  # считать количество значений
for i in range(k):  # заполняем очередь
    buf.append(int(input()))
for i in range(k, num):  # просматриваем оставшиеся элементы
    temp = int(input())
    if buf[cur] < min_a:
        min_a = buf[cur]  # обновляем минимальный элемент
    if (buf[cur] % 2 == 0) and (buf[cur] < min_e):
        min_e = buf[cur]  # обновляем минимальный чётный элемент
    if temp % 2 == 0:  # чётный элемент
        if temp * min_a < mp:  # умножаем на минимальный
            mp = temp * min_a
    else:  # temp % 2 == 1:  # нечётный элемент
        if temp * min_e < mp:  # умножаем на минимальный чётный
            mp = temp * min_e
    buf[cur] = temp  # обновляем первый элемент очереди и
    cur = (cur + 1) % k  # переходим к следующему элементу
if mp == 1002 * 1002:  # не нашли :-(
    mp = -1
print(mp)

sys.stdin = save_stdin