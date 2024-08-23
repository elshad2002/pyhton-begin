# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().
my_list = []
num = int(input("Введите сколько элеметов будет в вашем списке"))
a = 1
while a <= num:
    my_list.append(input(f"Введите {a}-й элемент списка"))
    a += 1
print(my_list)
for i in range(0, len(my_list), 2):
    if i + 1 >= len(my_list):
        break
    el = my_list[i]
    el_2 = my_list[i + 1]
    my_list.pop(i)
    my_list.insert(i, el_2)
    my_list.pop(i + 1)
    my_list.insert(i + 1, el)
print(my_list)
