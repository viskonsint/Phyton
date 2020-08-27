my_list = [777, 'Текст', False, 777.7, property, None]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)