# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке
with open("lesson5_2.txt", "r", encoding="utf-8") as les52:
    num = 0
    for line in les52:
        num_world = 0
        num += 1
        for i in line.split():
            num_world += 1
        print(f"Кол-во слов в {num} строке - {num_world}")
print(f"Кол-во строк в файле - {num} ")
