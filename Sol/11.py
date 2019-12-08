# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-11. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Школьная олимпиада по информатике проводилась для учеников 7-11-х
классов, участвующих в общем конкурсе. Каждый участник олимпиады мог
набрать от 0 до 70 баллов. Для определения призеров олимпиады сначала
отбираются 25% участников, показавших лучшие результаты. Если у
последнего участника, входящего в 25%, оказывается такое же количество
баллов, как и у следующих за ним в итоговой таблице, все они считаются
призерами только тогда, когда набранные ими баллы больше половины 
максимально возможных; иначе все они не считаются призерами.
Напишите эффективную по времени работы и по используемой памяти
программу, которая по результатам олимпиады будет определять
минимальный балл призера олимпиады, и количество призеров было в
каждой параллели (среди 7-х, 8-х, 9-х, 10-х и 11-х классов отдельно).
Гарантируется, что хотя бы одного призера по указанным правилам 
определить можно.
На вход программе сначала подается число участников олимпиады N. В
каждой из следующих N строк находится результат одного из участников
олимпиады в следующем формате:
     <Фамилия> <Имя> <класс> <баллы>
где <Фамилия> – строка, состоящая не более, чем из 30 символов, <Имя>
– строка, состоящая не более, чем из 15 символов, <класс> – число от 7
до 11, <баллы> – целое число от 0 до 70 набранных участником баллов.
<Фамилия> и <Имя>, <Имя> и <класс>, а также <класс> и <баллы> 
разделены одним пробелом. Пример входной строки:
    Семенов Сидор 11 66
Программа должна выводить в первой строке минимальный балл призера, а
в следующей – число призеров по всем параллелям отдельно. 
Пример выходных данных:
    63 
    1 5 8 12 22
"""
import sys, codecs
save_stdin = sys.stdin
sys.stdin = codecs.open("in/11.in", "r", "utf-8")

MAXBALL = 70
N = int(input())
res = {7:[], 8:[], 9:[], 10:[], 11:[]}
for i in range(N):
    fam, name, cls, ball = input().split()
    cls = int(cls); ball = int(ball)
    res[cls].append(ball)

total = []
for i in range(7,12):
    total = total + res[i]
total.sort(reverse = True)

n25 = len(total) // 4
if total[n25-1] == total[n25]:
    if total[n25] > MAXBALL // 2:
        best = [x for x in total if x >= total[n25]]
    else:
        best = [x for x in total if x > total[n25]]
else:
    best = total[0:n25]
print(best[-1])
for i in range(7,12):
    print(len([x for x in res[i] if x >= best[-1]]), end = " ")

sys.stdin = save_stdin