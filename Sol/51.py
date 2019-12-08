# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-51. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2014
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
По каналу связи передаются данные в виде последовательности положительных 
целых чисел. Количество чисел заранее неизвестно, но не менее двух, 
признаком конца данных считается число 0. После данных передаётся контрольное 
значение. Оно равно такому максимально возможному произведению двух чисел из 
переданного набора, которое делится на 7, но не делится на 49. Если такое 
произведение получить нельзя, контрольное значение считается равным 1.
Напишите эффективную, в том числе по памяти, программу, которая будет 
моделировать процесс приёма данных. Программа должна ввести все числа и 
контрольное значение и напечатать краткий отчёт, включающий количество принятых чисел, принятое контрольное значение, вычисленное контрольное значение и вывод о совпадении значений.
Описание входных данных
В каждой строке исходных данных содержится одно целое число. Сначала идут 
строки с основными данными – положительными числами, затем число 0 
(признак окончания данных), в последней строке – контрольное значение. 
Описание выходных данных
Программа должна вывести отчёт по форме, приведённой ниже в примере.
Пример входных данных:
6
7
8
9
0
64
Пример выходных данных для приведённого выше примера входных данных:
Введено чисел: 4
Контрольное значение: 64
Вычисленное значение: 63
Значения не совпали
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/51.in")

mx = 0 
max7 = 0  
count = 0
while True:
  x = int(input())
  if x == 0: break
  count += 1 
  if x % 7 == 0 and x % 49 != 0 and x > max7:
    max7 = x
  if x % 7 != 0  and  x > mx: mx = x        
R = int(input())
R1 = max7*mx
if R1 == 0: R1 = 1
print('Введено чисел:', count)
print('Контрольное значение:', R )
print('Вычисленное значение:', R1)
if R1 == R:
  print('Значения совпали')
else:
  print('Значения не совпали')

sys.stdin = save_stdin