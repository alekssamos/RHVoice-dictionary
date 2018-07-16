#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Скрипт для проверки предварительной обработки текста
#
# Сюда можно добавить определённым образом сформированные строки
# с известным результатом, например: "в 2000 г." -> "в двухтысячном году."
# Для проверки не сломалось ли чего после внесения изменений в templates.py.

from preprocessing.text_prepare import text_prepare

# набор фраз для проверки
test_txt=[
    # проверка шаблонов presamples
    ('Указанный ID используется', 'Указанный ай-ди используется.'),
    ('(см. главу 2)', '(смотри главу 2).'),
    ('I am', 'I am.'),
    ('МГТУ им. Н.Э. Баумана', 'МГТУ имени Н.Э. Баумана.'),
    ('градусов с.ш.', 'градусов северной широты.'),
    ('2 чел.', '2 человека.'),          # TODO нужно дополнить
    ('10 USD', '10 долларов США.'),
    ('$10', '10 долларов.'),
    ('принимаются €', 'принимаются евро.'),
    ('10,3 млн', '10 целых 3 десятых миллиона.'),
    ('I кв.', 'первый квартал.'),
    ('кв. 10', 'квартира 10.'),
    ('д. 10', 'дом 10.'),
    ('ул. 10', 'улица 10.'),
    ('пр-т', 'проспект.'),
    ('Тверская обл.', 'Тверская область.'),
    ('Московской обл.', 'Московской области.'),
    # Единицы измерения
    ('диаметром в 2 см', 'диаметром в 2 сантиметра.'),
    ('С 5 см до листа', 'С пяти сантиметров до листа.'),
    ('от 1 до 4 км', 'от одного до четырёх километров.'),
    ('около 20 м', 'около двадцати метров.'),
    ('в течение 21 сек', 'в течение двадцати одной секунды.'),
    ('порядка 10 шт.', 'порядка десяти штук.'),
    ('вес равен 65 кг', 'вес равен шестидесяти пяти килограммам.'),
    ('в 50 ₽', 'в пятидесяти рублях.'),
    ('4,5 км', '4 целых 5 десятых километра.'),
    ('18 МВт', '18 мегаватт.'),
    ('11 миллионов руб.', '11 миллионов рублей.'),
    ('тысяча шт.', 'тысяча штук.'),
    # Десятичные дроби
    ('1 234,345 567', '1234 целых 345567 миллионных.'),  
    ('по сравнению с 10,5 кг', 'по сравнению с десятью целыми пятью десятыми килограмма.'), 
    ('более 2,55 м', 'более двух целых пятидесяти пяти сотых метра.'),
    ('для 2,4 кВт', 'для двух целых четырёх десятых киловатта.'),
    ('равно 3,4 мм', 'равно трём целым четырём десятым миллиметра.'),
    ('при 3,5 тысячах', 'при трёх целых пяти десятых тысячах.'),
    # Римские цифры
    ('в XX веке', 'в двадцатом веке.'),
    #('CM', '900.'),
    #('XCIX', '99.'),
    # TODO нужно доделать дальнейшую проверку
    # проверка шаблонов samples
    ('220V', '220 вольт.'),
    ('2000 г.', 'двухтысячный год.'),
    ('2000 гг.', 'двухтысячные годы.'),
    ('2000-й г.', 'двухтысячный год.'),
    ('в 2000 г.', 'в двухтысячном году.'),
    ('в 2000 гг.', 'в двухтысячных годах.'),
    ('в 2000-х гг.', 'в двухтысячных годах.'),
    ('в 20 в.', 'в двадцатом веке.'),
    ('1 царя', 'одного царя.'),
    # Порядковые числительные
    # Склонение порядковых числительных при именах собственных
    ('Петр I', 'Петр первый.'),
    ('Фёдор I', 'Фёдор первый.'),
    ('Екатерина II', 'Екатерина вторая.'),
    ('при Николае II', 'при Николае втором.')
    # Время
    # Количественные числительные
    # Буквы греческого алфавита
    ]

count_err = 0    # счётчик непройдённых проверок

for txt in test_txt:
    text = text_prepare(txt[0])
    if text != txt[1]:
        print('ВНИМАНИЕ! неверное преобразование: "'+txt[0]+'" -> "'+text+'"'+'                 должно быть: "'+txt[1]+'"')
        count_err += 1

print('\nПройдено проверок: ' + str(len(test_txt)-count_err) + ' из ' + str(len(test_txt)) + '\n')

# дальше предлагается ввести текст вручную для проверки
txt = input('Введите текст:\n')

text = text_prepare(txt)

print('Обработанный текст:\n'+text)
