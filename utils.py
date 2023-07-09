import json
from datetime import datetime


def get_data(path):
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    new_data = []
    for transaction in data:
        if ('state' in transaction) and transaction['state'] == 'EXECUTED':
            new_data.append(transaction)
    return new_data


def get_sorted_data(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def get_formatted_data(data):
    old_data = data['date']
    date_transaction = datetime.strptime(old_data, "%Y-%m-%dT%H:%M:%S.%f")
    date_transaction = date_transaction.strftime("%d.%m.%Y")

    if 'from' in data:
        old_from = data['from']
        from_transaction = get_mask(old_from)
    else:
        from_transaction = ''

    old_to = data['to']
    to_transactions = get_mask(old_to)

    return f"""{date_transaction} {data['description']}
{from_transaction} -> {to_transactions}
{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"""


def get_mask(account_number):
    count_digit = sum(map(lambda x: x.isdigit(), account_number))
    if count_digit == 16:
        mask = account_number[:-12] + " " + account_number[-12:-10] + '** **** ' + account_number[-4:]
    else:
        mask = account_number[:5] + "**" + account_number[-4:]
    return mask
