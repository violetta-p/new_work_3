import json
from load_data import load_data
from src.funcs import *

data_file_name = "operations.json"  # Имя файла с данными о платежах

data_list = json.loads(load_data(data_file_name))  # Список с данными о платежах
sorted_data = get_sorted_data(data_list)  # Список с отсортированными по дате данными о платежах

counter = 0
for pay1 in sorted_data:
    if counter == 5:
        break
    if pay1["state"] == "EXECUTED":
        counter += 1
        print(get_presentation(get_all_data(pay1)))
