profit = int(input("Введите значение выручки за расчетный период: "))
loss = int(input("Введите значение убытков за расчетный период: "))
if profit > loss:
    print("Ваше предприятие прибыльно!")
    profitability = profit/loss
    print("Рентабельность выручки составляет:", profitability)
    worker = int(input("Введите кол-во работников: "))
    print("Прибыль на одного сотрудника составляет:", (profit/worker))
else:
    print("Ваше предприятие убыточно!")