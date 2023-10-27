from datetime import datetime
import json
import os


DATA_FILE = os.path.join('operations.json')


class Output_Of_Last_Five_Operations:
    def mask_card_number(self, card_number):
        """
        Разделяем данные карты получателя на название карты и счёт
        """
        for i, char in enumerate(card_number):
            if char.isdigit():
                break

        self.letters, self.numbers = card_number[:i], card_number[i:]

    def sender_card_number_format(self, data):
        """
        Возвращаем требуемый формат карты отправителя
        """

        self.mask_card_number(data)
        masked_numbers = "{} {}** **** {}".format(self.numbers[:4],
                                                  self.numbers[4:6],
                                                  self.numbers[-4:])
        return "{}{}".format(self.letters, masked_numbers)

    def receiver_card_number_format(self, data):
        """
        Возвращаем требуемый формат карты получателя
        """
        self.mask_card_number(data)
        masked_numbers = "**{}".format(self.numbers[-4:])
        return "{}{}".format(self.letters, masked_numbers)

    def start(self):

        with open(DATA_FILE) as f:
            data = json.load(f)

        # переводим строковый формат даты в объект datetime.
        for entry in data:
            entry["date"] = datetime.fromisoformat(entry["date"])

        # Фильтруем только выполненные операции и сортируем их по убыванию даты
        sorted_data = sorted(
            [entry for entry in data if entry["state"] == "EXECUTED"],
            key=lambda x: x["date"], reverse=True)

        # Выводим результат последний 5 выполненных операций
        for operation in sorted_data[:5]:
            print(f"{operation['date'].strftime('%d.%m.%Y')} "
                  f"{operation['description']}")
            print(
                f"{self.sender_card_number_format(operation['from'])}"
                if 'from' in operation
                else 'N/A',
                f"-> {self.receiver_card_number_format(operation['to'])}"
                )
            print(operation['operationAmount']['amount'],
                  operation['operationAmount']['currency']['name'])
            print()


execute_code = Output_Of_Last_Five_Operations()
execute_code.start()
