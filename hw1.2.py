seconds = int(input("Введите кол-во секунд: "))
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print("%d:%02d:%02d" % (hour, minutes, seconds))