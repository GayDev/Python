# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-71. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2017
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
71) (Д.Ф. Муфаззалов) На вход программы поступает 
последовательность из N натуральных целых чисел, каждое 
из которых не больше 1000. Требуется определить, можно 
ли записать все значащие цифры шестнадцатеричной записи 
этих чисел так, чтобы полученная строка было симметричной 
(читалась одинаково как слева направо, так и справа налево). 
Если требуемую строку составить невозможно, то программа 
должна вывести на экран число 0, а если возможно, то 
вывести число 1.
Входные данные:
  На вход программе подаётся натуральное число N (N <= 1000), 
  а затем N натуральных чисел, каждое из которых не 
  превышает 10000. 
Пример входных данных: 
  3 
  13
  22
  32
Пример выходных данных для приведённого примера входных данных:
  0
Из цифр D, 1, 6, 2, 0 нельзя составить симметричную строку.
Пример входных данных: 
  4
  186
  68
  171
  14
Пример выходных данных для приведённого примера входных данных:
  1
Из цифр A, B, 4, 4, A, B, D можно составить симметричную строку.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/71.in")

count = [0]*16
N = int(input())
for i in range(N):
  x = int(input())
  while x > 0:
    c = x % 16
    count[c] += 1
    x //= 16

i = 0
check = 0;
while i <= 15 and check < 2:
  check += count[i] % 2
  i += 1

print( int(check < 2) );

sys.stdin = save_stdin