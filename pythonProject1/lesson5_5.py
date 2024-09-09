# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open("lesson5_5.txt", "r+", encoding="utf-8") as less55:
    less55.write("45 15 22 28 10 30")
with open("lesson5_5.txt", "r+", encoding="utf-8") as less55:
    result = 0
    for line in less55:
        num_list = line.split()
        for i in num_list:
            result += int(i)
print(result)
