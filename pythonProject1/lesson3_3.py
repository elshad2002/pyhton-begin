# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.
def my_func(var_1, var_2, var_3):
    '''возвращает сумму наибольших двух аргументов'''
    var_list = [var_1, var_2, var_3]
    max_el = max(var_list)
    var_list.remove(max_el)
    max_el_2 = max(var_list)
    return max_el + max_el_2


print(my_func(6, 4, 6))
