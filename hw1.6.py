a = int(input("Введите результат пробежки первого дня: "))
b = int(input("Введите дистанцию которую вы хотели бы пробежать: "))
d = 1
while b >= a:
    print(d, "-й день:", "{:.2f}".format(a))
    a = 1.1 * a
    d += 1
print("Вы достигнете нужного результата прибавляя к дистанции каждого предыдущего дня по 10% через:", d, "дней!")

