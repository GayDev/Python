# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-86. 
Решение на языке Python 3.
Автор: Константин Поляков, 2018
-------------------------------------------------
86) (О.Л. Дуркин)
На вход программы поступает последовательность из N целых положительных 
чисел. Необходимо определить количество троек элементов (ai, aj, ak) 
этого набора, в которых 1 <= i < j < k <= N и сумма элементов кратна 
7 и нечётна. 
Пример входных данных:
7 
8 
11 
14 
15 
2 
4 
7
Пример выходных данных для приведённого выше примера входных данных:
2
В приведённом наборе из 7 чисел имеются две тройки (8, 11, 2) и 
(15, 2, 4), сумма элементов которых кратна 7 и нечетна.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/86.in")

N = int(input())
A = [0]*N
for i in range(0, N) :
  A[i] = int(input())

count = 0
for i in range(0, N-2) :
  for j in range(i+1, N-1) :
    for k in range(j+1, N) :
      summa = A[i]+A[j]+A[k]
      if summa % 7 == 0  and  summa % 2 != 0:
        count += 1
print(count)

sys.stdin = save_stdin