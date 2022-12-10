from random import sample
from string import ascii_letters, digits


def get_random_password() -> str:
    n = 8
    password = sample((*ascii_letters, *digits), n)  # используем отдельные объекты модуля string (алфавит + цифры)
    return ''.join(password)  # cборка строки из списка


print(get_random_password())
                    # конец кода