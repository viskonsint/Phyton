seasons_list = ['зима', "весна","лето","осень"]
seasons_dict = {1 : 'январь', 2 : 'февраль', 3 : 'март', 4 : 'апрель', 5:"май", 6:"июнь", 7: "июль", 8:"август", 9:"сентябрь",10:"октябрь",11:"ноябрь", 12: "декабрь"}
month = int(input("Введите номер месяца "))
if month ==1:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 2:
    print(seasons_dict.get(2))
    print(seasons_list[0])
elif month == 3:
    print(seasons_dict.get(3))
    print(seasons_list[1])
elif month == 4:
    print(seasons_dict.get(4))
    print(seasons_list[1])
elif month == 5:
    print(seasons_dict.get(5))
    print(seasons_list[1])
elif month == 6:
    print(seasons_dict.get(6))
    print(seasons_list[2])
elif month == 7:
    print(seasons_dict.get(7))
    print(seasons_list[2])
elif month == 8:
    print(seasons_dict.get(8))
    print(seasons_list[2])
elif month == 9:
    print(seasons_dict.get(9))
    print(seasons_list[3])
elif month == 10:
    print(seasons_dict.get(10))
    print(seasons_list[3])
elif month == 11:
    print(seasons_dict.get(11))
    print(seasons_list[3])
elif month == 12:
    print(seasons_dict.get(12))
    print(seasons_list[0])
else:
        print("Вы введи неверные данные")