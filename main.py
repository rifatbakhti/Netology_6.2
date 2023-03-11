from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)



## 1. Выполните пункты 1-3 задания.
## Ваш код

name_pattern = r'([А-ЯЁ][а-яё]+)(?:,|\s)([А-ЯЁ][а-яё]+)(?:,|\s)([А-ЯЁ][а-яё]+)'
list_re = []
for contact in contacts_list:
    list_re.append(re.sub(name_pattern, r'\1 \2 \3', contact[0]))
print(list_re)


## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)