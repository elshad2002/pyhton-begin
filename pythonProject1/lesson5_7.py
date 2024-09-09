# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# ример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
average_profit = 0
divider = 0
result_list = [{}, {}]
with open("lesson5_7.txt", "r", encoding="utf-8") as less57:
    for line in less57:
        profit = 0
        line_list = line.split()
        profit = int(line_list[2]) - int(line_list[3])
        if profit > 0:
            average_profit += profit
            divider += 1
        result_list[0].update({line_list[0]: abs(profit)})
    average_profit = average_profit / divider
    result_list[1].update({"average profit": average_profit})
print(result_list)
with open("lesson5_7.json", "w", encoding="utf-8") as les_js:
    les_js.write(f"{result_list}")
