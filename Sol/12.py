# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-12. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
В некотором вузе абитуриенты проходили предварительное тестирование, по
результатам которого они могут быть допущены к сдаче вступительных
экзаменов в первом потоке. Тестирование проводится по трём предметам, по 
каждому предмету абитуриент может набрать от 0 100 баллов. При этом к
сдаче экзаменов в первом потоке допускаются абитуриенты, набравшие по
результатам тестирования не менее 30 баллов по каждому из трёх
предметов, причём сумма баллов должна быть не менее 140. На вход 
программы подаются сведения о результатах предварительного тестирования.
Известно, что общее количество участников тестирования не превосходит
500. 
В первой строке вводится количество абитуриентов, принимавших участие в
тестировании, N. Далее следуют N строк, имеющих следующий формат: 
<Фамилия> <Имя> <Баллы>
Здесь <Фамилия> – строка, состоящая не более чем из 20 символов; <Имя>
– строка, состоящая не более чем из 15 символов, <Баллы> – строка,
содержащая два целых числа, разделенных пробелом – баллы, полученные на
тестировании по каждому из трёх предметов. При этом <Фамилия> и <Имя>,
<Имя> и <Баллы> разделены одним пробелом. Пример входной строки:
    Романов Вельямин 48 39 55
Напишите программу, которая будет выводить на экран фамилии и имена
абитуриентов, допущенных к сдаче экзаменов в первом потоке. При этом 
фамилии должны выводиться в алфавитном порядке.
"""
import sys, codecs
save_stdin = sys.stdin
sys.stdin = codecs.open("in/12.in", "r", "utf-8")

N = int(input())
accepted = []
for i in range(N):
    fam, name, b1, b2, b3 = input().split()
    ball = [int(x) for x in [b1, b2, b3]]
    if ball[0] >= 30 and ball[1] >= 30 and ball[2] >= 30 and sum(ball) >= 140:
        accepted.append(fam+" "+name)
for x in sorted(accepted): 
    print(x)

sys.stdin = save_stdin