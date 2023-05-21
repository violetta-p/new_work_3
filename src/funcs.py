import datetime


def get_sorted_data(data_list):
    """
    Принимает на вход исходный массив с данными.
    Возвращает массив с отсортированными от недавних к более старым платежам данными.
    """
    cleaned_data = [i for i in data_list if i] # В json файле есть "пробелы" в данных. Данное действие убирает эти "пробелы"
    sorted_list = sorted(cleaned_data,
                     key=lambda x: datetime.datetime.strptime(" ".join(x["date"].split("T")), "%Y-%m-%d %H:%M:%S.%f"),
                     reverse=True)
    return sorted_list


def get_date(data):
    """
    Возвращает дату платежа в формате ДД.ММ.ГГГГ
    """
    data_str = data.split("T")
    data_format = datetime.date.fromisoformat(data_str[0])
    return data_format.strftime("%d.%m.%Y")


def get_description(data):
    """
    Возвращает Информацию о платежах, если она есть.
    Возвращает "No description", если данных нет
    """
    if data is not None:
        return data
    return "No description"


def get_sender(sender_info):
    """
    Возвращает данные отправителя в формате XXXX XX** **** XXXX,
    если они есть. Если данных нет, возвращает сообщение 'No info about sender'
    """
    if sender_info is not None:
        card_data = sender_info.split(" ")
        card_info = " ".join(card_data[:-1])
        card_number = list(card_data[-1])
        card_number[-10:-4] = "******"
        card_number = "".join(card_number)
        new_number = ''
        for i in range(0, len(card_number), 4):
            new_number += card_number[i:i+4]
            new_number += ' '

        return f'{card_info} {new_number.rstrip(" ")}'
    return "No info about sender"


def get_recipient(recipient_info):
    """
    Возвращает данные получателя в формате 'Счет **XXXX'.
    """
    if recipient_info is not None:
        card_data = recipient_info.split(" ")
        card_number = list(card_data[-1])
        card_number = "".join(card_number[-4:])
        card_info = " ".join(card_data[:-1])
        return f'{card_info} **{card_number}'
    return "No info about recipient"


def get_amount(amount_info):
    """
    Возвращает сумму платежа с указанием валюты
    """
    summ = amount_info["amount"]
    currency_ = amount_info["currency"]["name"]
    return f'{summ} {currency_}'


def get_all_data(payment):
    """
    Принимает элемент исходного массива с данными.
    Возвращает все данные в виде кортежа
    tuple = (transaction_date, description, sender_info, recipient_info, amount)
    """
    transaction_date = get_date(payment.get("date", None))
    description = get_description(payment.get("description", None))
    sender_info = get_sender(payment.get("from", None))
    recipient_info = get_recipient(payment.get("to", None))
    amount = get_amount(payment.get("operationAmount", None))
    return transaction_date, description, sender_info, recipient_info, amount


def get_presentation(tuple_with_data):
    """
    Приминает кортеж с данными вида
    typle = (transaction_date, description, sender_info, recipient_info, amount).
    Возвращает данные в формате для вывода на экран
    """
    return f'{tuple_with_data[0]} {tuple_with_data[1]}\n'\
           f'{tuple_with_data[2]} -> {tuple_with_data[3]}\n'\
           f'{tuple_with_data[4]}\n'
