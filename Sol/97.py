# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-97.
Решение на языке Python 3.
-------------------------------------------------
97) (А.А. Богданов, Danov1802 №27-4) На вход 
программы поступает последовательность из N целых 
положительных чисел. Рассматриваются все пары 
различных элементов последовательности (элементы 
пары не обязаны стоять в последовательности рядом, 
порядок элементов в паре не важен). Необходимо 
определить количество пар, сумма которых кратна 3, 
а произведение кратно 5. На вход алгоритма подается 
число N и далее сами N чисел.
Описание входных и выходных данных
В первой строке входных данных задаётся количество 
чисел N (1 ≤ N ≤ 1000). В каждой из последующих N 
строк записано одно натуральное число, не превышающее 
10000. В качестве результата программа должна вывести 
одно число: количество найденных пар.
Пример входных данных №1:
10 
1 2 3 4 5 6 7 8 9 10
Выходные данных для приведенного выше примера: 6
Найденные пары для примера : {(1;5) (2;10) (4;5) (5;7) (5;10) (8;10)}
Пример входных данных №2:
23 
71 33 87 66 37 97 91 30 52 19 56 85 81 27 25 35 47 72 85 87 98 88 41
Выходные данных для приведенного выше примера: 31
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/97.in")

def sign( n ):
  if n > 0: return 1
  elif n < 0: return -1
  else: return 0
  
s = [[0, 0, 0], [0, 0, 0]]

n = int( input() )
for i in range(n):
  a = int( input() )
  s[sign(a % 5)][a % 3] += 1

ans = (s[0][0]*(s[0][0]-1) // 2 
    + s[0][0]*s[1][0] 
    + s[0][1]*(s[0][2]+s[1][2])
    + s[0][2]*s[1][1])

print(ans)

sys.stdin = save_stdin