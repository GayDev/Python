# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-46. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На плоскости дан набор точек с целочисленными координатами. Необходимо 
найти треугольник наибольшей площади с вершинами в этих точках, одна из
сторон которого лежит на оси OX. Напишите эффективную, в том числе по 
памяти, программу, которая будет решать эту задачу. Размер памяти,
которую использует Ваша программа, не должен зависеть от длины 
переданной последовательности чисел. Укажите используемый язык
программирования и его версию.
В первой строке вводится одно целое положительное число – количество 
точек N. Каждая из следующих N строк содержит два целых числа – сначала 
координата х, затем координата у очередной точки.
Программа должна вывести одно число – максимальную площадь треугольника,
удовлетворяющего условиям задачи. Если такого треугольника не
существует, программа должна вывести ноль.
Пример входных данных:
    6
    0 0
    2 0
    0 4
    3 3
    5 5 
    -6 -6
Пример выходных данных для приведенного выше примера входных данных:
    6
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/46.in")

N = int(input())
xMin = None 
xMax = 0; yMax = 0
for i in range(N):
    x, y = [int(v) for v in input().split()]
    if y == 0:
      if xMin == None or x > xMax: 
        xMax = x
      if xMin == None or x < xMin: 
        xMin = x
    else: 
        yMax = max( abs(y), yMax )
print((xMax - xMin) * yMax / 2.)

sys.stdin = save_stdin