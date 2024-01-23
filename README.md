## Функционал скрипта.
 - Выводятся последние 5 выполненных (EXECUTED) операций на экран.
 - Операции разделены пустой строкой.
 - Дата перевода в формате ДД.ММ.ГГГГ (пример 14.10.2018).
 - Сверху списка выводятся последние операции (по дате).
 - Номер карты выводится в формате XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
 - Номер счета выводится в формате **XXXX (видны только последние 4 цифры номера счета).
 - Если операция - открытие вклада, вместо счёта отправителя указывается N/A
## Результат выполнения скрипта с имеющимися данными:
```
08.12.2019 Открытие вклада
N/A -> Счет **5907
41096.24 USD

07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет 3861 14** **** 9794 -> Счет **8125
62814.53 руб.

05.11.2019 Открытие вклада
N/A -> Счет **8381
21344.35 руб.
```
