# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл
translate = ["Один", "Два", "Три", "Четыре"]
with open("lesson5_4.txt", "r", encoding="utf-8") as less54:
    num = 0
    for line in less54:
        num_list = line.split("-")
        num_list[0] = translate[num]
        with open("lesson5_4_1.txt", "a", encoding="utf-8") as new_less54:
            new_less54.write(" - ".join(num_list))
        num += 1
