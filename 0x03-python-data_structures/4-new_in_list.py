#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lista = my_list.copy()
    if 0 <= idx <= len(my_list)-1:
        lista[idx] = element
    return lista
