# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-demo-2014. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
По каналу связи передаётся последовательность положительных целых
чисел, все числа не превышают 1000. Количество чисел известно, но может
быть очень велико. Затем передаётся контрольное значение
последовательности – наибольшее число R, удовлетворяющее следующим
условиям:
  1) R – произведение двух различных переданных элементов
     последовательности («различные» означает, что не рассматриваются
     квадраты переданных чисел; допускаются произведения различных
     элементов последовательности, равных по величине);
  2) R делится на 21.
Если такого числа R нет, то контрольное значение полагается равным 0.
В результате помех при передаче как сами числа, так и контрольное значение
могут быть искажены.
Напишите эффективную, в том числе по используемой памяти, программу
(укажите используемую версию языка программирования, например, Borland
Pascal 7.0), которая будет проверять правильность контрольного значения.
Программа должна напечатать отчёт по следующей форме:
Вычисленное контрольное значение: …
Контроль пройден (или – Контроль не пройден)
Перед текстом программы кратко опишите используемый Вами алгоритм
решения.
На вход программе в первой строке подаётся количество чисел N. В каждой
из последующих N строк записано одно натуральное число, не превышающее
1000. В последней строке записано контрольное значение.
Пример входных данных:
6
70
21
997
7
9
300
21000
Пример выходных данных для приведённого выше примера входных данных:
Вычисленное контрольное значение: 21000
Контроль пройден
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/demo-2014.in")

N = int(input())
M3 = M7 = M21 = M = 0
for i in range(N):
    x = int(input())
    if x % 21 != 0:
        if x % 3 == 0: M3 = max(M3, x)
        if x % 7 == 0: M7 = max(M7, x)
    if x % 21 == 0  and  x > M21: 
        M = max(M21, M)
        M21 = x
    else:
        M = max(M, x)        
R0 = int(input())
R = max(M3*M7, M21*M)
if R == R0:
    print("Контроль пройден")
else:
    print("Контроль не пройден")


sys.stdin = save_stdin