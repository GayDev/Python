# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-52. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2014
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Дед Мороз и Снегурочка приходят на детские утренники с мешком конфет. 
Дед Мороз делит конфеты поровну между всеми присутствующими детьми (детей 
на утреннике никогда не бывает больше 100), а оставшиеся конфеты отдает 
Снегурочке. Снегурочка каждый раз записывает в блокнот количество полученных 
конфет. Если конфеты разделились между всеми детьми без остатка, Снегурочка 
ничего не получает и ничего не записывает. Когда утренники закончились, 
Деду Морозу стало интересно, какое число чаще всего записывала Снегурочка. 
Дед Мороз и Снегурочка – волшебные, поэтому число утренников N, на которых 
они побывали, может быть очень большим.
Напишите программу, которая будет решать эту задачу. Перед текстом программы 
кратко опишите алгоритм решения задачи и укажите используемый язык 
программирования и его версию.
Желательно, чтобы программа была эффективной как по времени работы, так и 
по используемой памяти. Программу будем считать эффективной по памяти, если 
используемая память не зависит от размера входных данных (то есть числа 
утренников). Программу будем считать эффективной по
времени, если при увеличении размера входных данных N в t раз (t – любое 
число) время её работы увеличивается не более чем в t раз. 
Описание входных данных
В первой строке вводится одно целое положительное число – количество 
утренников N.
Каждая из следующих N строк содержит два целых числа: сначала D – количество 
пришедших на очередной утренник детей, а затем K – количество конфет в мешке 
Деда Мороза на этом утреннике. Гарантируется выполнение следующих соотношений:
1 ≤ N ≤ 10000
1 ≤ D ≤ 100 (для каждого D)
D ≤ K ≤ 1000 (для каждой пары D, K)
Описание выходных данных
Программа должна вывести одно число – то, которое Снегурочка записывала чаще 
всего. Если несколько чисел записывались одинаково часто, надо вывести большее 
из них. Если Снегурочка ни разу ничего не записывала, надо вывести ноль.
Пример входных данных:
7
10 58
15 315
20 408
100 1000
32 63
32 63
11 121
Пример выходных данных для приведённого выше примера входных данных:
31
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/52.in")

N = int(input())
count = {}
for i in range(N):
  D, K = map(int, input().split())
  ost = K % D
  if ost > 0:
    count[ost] = count.get(ost, 0) + 1

if len(count) == 0:
  print(0)
else:  
  nMax = 0
  for k, v in count.items():
    if nMax == 0  or  count[k] >= count[nMax]:
      nMax = k
  print(nMax)

sys.stdin = save_stdin