﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-43. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На ускорителе для большого числа частиц производятся замеры скорости
каждой из них. Все скорости положительны. Чтобы в документации 
качественно отличать одну серию эксперимента от другой каждую серию
решили характеризовать числом равным минимальной чётной сумме из всех
сумм пар скоростей различных частиц. Если чётная сумма отсутствует, то 
характеристикой будет являться просто минимальная сумма. 
Вам предлагается написать эффективную, в том числе по используемой
памяти, программу (укажите используемую версию языка программирования),
которая будет обрабатывать результаты эксперимента, находя искомую 
величину. Следует учитывать, что частиц, скорость которых измерена,
может быть очень много, но не может быть меньше двух.
Перед текстом программы кратко опишите используемый вами алгоритм 
решения задачи.
На вход программе в первой строке подается количество частиц N. В каждой
из последующих N суток записано одно натуральное число не превышающее
30000.
Пример входных данных:
    5
    123
    1000
    12
    2548
    12
Программа должна вывести характеристику данной серии экспериментов. 
Пример выходных данных для приведенного выше примера входных данных:
    24
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/43.in")

N = int(input())
ch1 = 60001; ch2 = 60001
nch1 = 60001; nch2 = 60001
for i in range(N):
    v = int(input())
    if v % 2 == 0:
        if v < ch1:
            ch2 = ch1; ch1 = v
        elif v < ch2: ch2 = v
    elif v < nch1:
        nch2 = nch1; nch1 = v
    elif v < nch2: nch2 = v   

if ch2 == nch2: 
    print(ch1+nch1)
else:
    if ch1+ch2 < nch1+nch2:
        print(ch1+ch2)  
    else:
        print(nch1+nch2)  

sys.stdin = save_stdin