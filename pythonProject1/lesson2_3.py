# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict
season = {"Winter": [12, 1, 2], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}
user_num = int(input("Enter month number"))
for k, v in season.items():
    if user_num in v:
        print(f"Your season is {k}")
