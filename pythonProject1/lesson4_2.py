# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его
# формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
# my_numbers = []
from random import randint

my_numbers = [randint(0, 1000) for i in range(10)]
result_list = [my_numbers[i + 1] for i in range(len(my_numbers) - 1) if my_numbers[i + 1] > my_numbers[i]]
print(my_numbers)
print(result_list)
