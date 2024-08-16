revenue = int(input("Введите выручку вашей фирмы:"))
costs = int(input("Введите издержки фирмы:"))
if revenue > costs:
    print("Вы работаете в плюс!")
    profit = revenue - costs
    rent = profit / revenue * 100
    print(f"Прибыль в вашей фирме: {profit}")
    print(f"Рентабельность вашей фирмы: {rent:.0f}%")
    personal = int(input("Введите количесво сотрудников в вашей фирме:"))
    profit_personal = profit / personal
    print(f"Ваша прибыль в расчете на одного сотрудника: {profit_personal:.0f}")
else:
    print("Вы работаете в минус, закрывайтесь")
