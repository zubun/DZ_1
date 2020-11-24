# #name = input("Введите ваше имя: ")
# surname = input("Введите вашу фамилию: ")
# age = int(input("Сколько вам полных лет: "))
# print("Вас зовут", name, surname, ". Вам", age, "лет." )
# seconds = int(input("Введите кол-во секунд: "))
# hour = seconds // 3600
# seconds %= 3600
# minutes = seconds // 60
# seconds %= 60
# print("%d:%02d:%02d" % (hour, minutes, seconds))
# number = input("Введите число: ")
# number_1 = int(number + number)
# number_2 = int(number + number + number)
# print(int(number) + number_1 + number_2)


# n = abs(int(input("Введите целое положительное число ")))
# max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max)
#         break
# i = 3481561
# s = str(i)
# ls = list(map(int, s))
# r = max(ls)
# print(r)

# profit = int(input("Введите значение выручки за расчетный период: "))
# loss = int(input("Введите значение убытков за расчетный период: "))
# if profit > loss:
#     print("Ваше предприятие прибыльно!")
#     profitability = profit/loss
#     print("Рентабельность выручки составляет:", profitability)
#     worker = int(input("Введите кол-во работников: "))
#     print("Прибыль на одного сотрудника составляет:", (profit/worker))
# else:
#     print("Ваше предприятие убыточно!")
a = int(input("Введите результат пробежки первого дня: "))
b = int(input("Введите дистанцию которую вы хотели бы пробежать: "))
d = 1
while b >= a:
    print(d, "-й день:", "{:.2f}".format(a))
    a = 1.1 * a
    d += 1
print("Вы достигнете нужного результата прибавляя к дистанции каждого предыдущего дня по 10% через:", d, "дней!")



