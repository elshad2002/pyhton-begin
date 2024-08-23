# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
my_list = [5, 4, 4, 2, 1]
user_ans = int(input("enter new element of rating"))
try:
    for i in range(len(my_list)):
        if user_ans >= my_list[i]:
            my_list.insert(i, user_ans)
            break
        if my_list[i] >= user_ans and my_list[i + 1] <= user_ans:
            my_list.insert(i + 1, user_ans)
            break
except:
    my_list.append(user_ans)
print(my_list)
