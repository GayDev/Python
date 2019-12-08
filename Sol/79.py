# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-79.
Решение на языке Python 3.
 Автор: Д.В. Богданов, 2017
-------------------------------------------------
79) (Д.В. Богданов)
Дан набор из Т натуральных чисел. Необходимо определить количество троек
элементов (ai, aj, ak) этого набора, в которых 1 ≤ i < j < k ≤ N
и сумма элементов кратна 12.
Напишите эффективную по времени и по памяти программу для решения
этой задачи. Программа считается эффективной по времени, если при увеличении
количества исходных чисел N в k раз время работы программы увеличивается
не более чем в k раз. Программа считается эффективной по памяти, если память,
необходимая для хранения переменных программы, не превышает одного килобайта
и не увеличивается с ростом N.
Описание входных и выходных данных
В первой строке входных данных задаётся количество чисел N
(3 ≤ N ≤ 10000). В каждой из последующих N строк записано одно натуральное
число, не превышающее 1000.
Пример входных данных:
5
7
5
6
12
24
Пример выходных данных для приведённого выше примера входных данных:
2
В приведённом наборе из 5 чисел имеются две тройки — (7, 5, 12) и (7, 5, 24),
сумма элементов которых кратна 12.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/79.in")

N = int(input())
rem = [0]*12
for i in range(N):
  x = int(input())
  rem[x % 12] += 1

count = 0
for i in range(12):
  for j in range(i,12):
    k = (24 - i - j) % 12
    if k >= j:
      if i == j == k:
        count += rem[i]*(rem[i]-1)*(rem[i]-2)//6
      elif i == j:
        count += rem[i]*(rem[i]-1)*rem[k]//2
      elif i == k:
        count += rem[i]*rem[j]*(rem[i]-1)//2
      elif j == k:
        count += rem[i]*rem[j]*(rem[j]-1)//2
      else:
        count += rem[i]*rem[j]*rem[k]
print(count)

sys.stdin = save_stdin