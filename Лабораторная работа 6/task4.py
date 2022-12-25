import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        json_dict = []
        for i, line in enumerate(f):  # получаем пары индекс-значение
            # далее формируем поле,удалив вокруг значения и отделив его запятой:
            fields = line.strip(new_line).split(delimiter)

            if i == 0:
                title = fields  # поля первой строки - это заголовки
                continue

            json_dict.append({})  # добавляем словарь в таблицу

            for i, line in enumerate(title):
                json_dict[-1][title[i]] = fields[i]
    return json_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# конец кода