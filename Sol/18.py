﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-18. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Имеется список результатов голосования избирателей за несколько
партий, в виде списка названий данных партий. На вход программе в
первой строке подается количество избирателей в списке N. В каждой из
последующих N строк записано название партии, за которую проголосовал 
данный избиратель, в виде текстовой строки. Длина строки не
превосходит 50 символов, название может содержать буквы, цифры,
пробелы и прочие символы.
Пример входных данных:
    6
    Party one
    Party two
    Party three
    Party three
    Party two
    Party three
Программа должна вывести список всех партий, встречающихся в исходном
списке, в порядке убывания количества голосов, отданных за эту партию.
При этом название каждой партии должно быть выведено ровно один раз,
вне зависимости от того, сколько голосов было отдано за данную партию.
Пример выходных данных для приведенного выше примера входных данных:
    Party three
    Party two
    Party one
При этом следует учитывать, что количество голосов избирателей в
исходном списке может быть велико (свыше 1000), а количество различных
партий в этом списке не превосходит 10.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/18.in")

N = int(input())
pList = {}
for i in range(N):
    pName = input()
    pList[pName] = pList.get(pName, 0) + 1
pList = sorted(pList.items(), key = lambda x: x[1], reverse = True)
for p in pList:
    print(p[0])

sys.stdin = save_stdin