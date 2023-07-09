from utils import get_data, get_filtered_data, get_sorted_data, get_formatted_data, get_mask


def test_get_filtered_data():
    assert len(get_filtered_data([{"state": "EXECUTED"}, {"state": "CANCELED"}, {}])) == 1


def test_get_sorted_data():
    assert (get_sorted_data([{'date': "2018-04-04T17:33:34.701093"}, {'date': "2019-03-23T01:09:46.296404"}, {
        'date': "2019-12-08T22:46:21.935582"}])) == [{'date': '2019-12-08T22:46:21.935582'}, {
        'date': '2019-03-23T01:09:46.296404'}, {'date': '2018-04-04T17:33:34.701093'}]


def test_get_formatted_data():
    assert (get_formatted_data({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
    })) == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."
    assert (get_formatted_data({
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
    })) == "23.03.2018 Открытие вклада\n -> Счет **2431\n48223.05 руб."


def test_get_mask():
    assert (get_mask("Счет 44812258784861134719")) == "Счет **4719"
    assert (get_mask("MasterCard 7158300734726758")) == "MasterCard 7158 30** **** 6758"
