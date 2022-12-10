from pprint import pprint


def func(i):
    dict_bin = {'bin': bin(i)}  # создаём отдельные словари
    dict_hex = {'hex': hex(i)}
    dict_oct = {'oct': oct(i)}
    dict_dec = {'dec': i}
    dict_ = dict_bin | dict_dec | dict_hex | dict_oct  # объединеняем словари в один
    return dict_


list_comprehension = [func(i) for i in range(0, 16)]  # для дальнейшего вывода словаря для чисел от 0 до 15 вкл.

pprint(list_comprehension)
                    # конец кода
