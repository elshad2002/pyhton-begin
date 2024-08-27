# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.
def UserInfo(name, surname, date_of_burn, city, email, phone):
    return f"Name-{name} Surname-{surname}, Burn-{date_of_burn}, City-{city}, email-{email}, phone-{phone}"


print(UserInfo(name="Ivan", email="ivanov@yandex.ru", surname="Ivanov", date_of_burn="20.02.2000", phone="89772673912",
               city="Moscow"))
