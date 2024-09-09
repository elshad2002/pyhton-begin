# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.
user_data = "0"
while user_data != "":
    user_data = input("enter your data: ")
    with open("lesson5_1.txt", "a+", encoding="utf-8") as les5:
        les5.write(f"{user_data}\n")
