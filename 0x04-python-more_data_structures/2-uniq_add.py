#!/usr/bin/python3
def uniq_add(my_list=[]):
    lista = list(set(my_list))

    sum = 0

    for i in lista:
        sum += i

    return sum
