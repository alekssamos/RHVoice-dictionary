#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Скрипт предварительной обработки текста для
# синтезатора речи RHVoice Ольги Яковлевой
# By Capricorn2001

from re import sub, findall

i_mu = (
  (
    (
      (
        'нулевой',
        'тысячный',
        'двухтысячный',
        'трёхтысячный',
        'четырёхтысячный',
        'пятитысячный',
        'шеститысячный',
        'семитысячный',
        'восьмитысячный',
        'девятитысячный'
      ),
      'сотый',
      'двухсотый',
      'трёхсотый',
      'четырёхсотый',
      'пятисотый',
      'шестисотый',
      'семисотый',
      'восьмисотый',
      'девятисотый'
    ),
    'десятый',
    'двадцатый',
    'тридцатый',
    'сороковой',
    'пятидесятый',
    'шестидесятый',
    'семидесятый',
    'восьмидесятый', 
    'девяностый'
  ),
  ('первый', 'одиннадцатый'),
  ('второй', 'двенадцатый'),
  ('третий', 'тринадцатый'),
  ('четвёртый', 'четырнадцатый'),
  ('пятый', 'пятнадцатый'),
  ('шестой', 'шестнадцатый'),
  ('седьмой', 'семнадцатый'),
  ('восьмой', 'восемнадцатый'),
  ('девятый', 'девятнадцатый')
)
i_sr = (
  (
    (
      (
        'нулевое',
        'тысячное',
        'двухтысячное',
        'трёхтысячное',
        'четырёхтысячное',
        'пятитысячное',
        'шеститысячное',
        'семитысячное',
        'восьмитысячное',
        'девятитысячное'
      ),
      'сотое',
      'двухсотое',
      'трёхсотое',
      'четырёхсотое',
      'пятисотое',
      'шестисотое',
      'семисотое',
      'восьмисотое',
      'девятисотое'
    ),
    'десятое',
    'двадцатое',
    'тридцатое',
    'сороковой',
    'пятидесятое',
    'шестидесятое',
    'семидесятое',
    'восьмидесятое', 
    'девяностое'
  ),
  ('первое', 'одиннадцатое'),
  ('второе', 'двенадцатое'),
  ('третье', 'тринадцатое'),
  ('четвёртое', 'четырнадцатое'),
  ('пятое', 'пятнадцатое'),
  ('шестое', 'шестнадцатое'),
  ('седьмое', 'семнадцатое'),
  ('восьмое', 'восемнадцатое'),
  ('девятое', 'девятнадцатое')
)
i_zh = (
  (
    (
      (
        'нулевая',
        'тысячная',
        'двухтысячная',
        'трёхтысячная',
        'четырёхтысячная',
        'пятитысячная',
        'шеститысячная',
        'семитысячная',
        'восьмитысячная',
        'девятитысячная'
      ),
      'сотая',
      'двухсотая',
      'трёхсотая',
      'четырёхсотая',
      'пятисотая',
      'шестисотая',
      'семисотая',
      'восьмисотая',
      'девятисотая'
    ),
    'десятая',
    'двадцатая',
    'тридцатая',
    'сороковой',
    'пятидесятая',
    'шестидесятая',
    'семидесятая',
    'восьмидесятая', 
    'девяностая'
  ),
  ('первая', 'одиннадцатая'),
  ('вторая', 'двенадцатая'),
  ('третья', 'тринадцатая'),
  ('четвёртая', 'четырнадцатая'),
  ('пятая', 'пятнадцатая'),
  ('шестая', 'шестнадцатая'),
  ('седьмая', 'семнадцатая'),
  ('восьмая', 'восемнадцатая'),
  ('девятая', 'девятнадцатая')
)
i_mn = (
  (
    (
      (
        'нулевые',
        'тысячные',
        'двухтысячные',
        'трёхтысячные',
        'четырёхтысячные',
        'пятитысячные',
        'шеститысячные',
        'семитысячные',
        'восьмитысячные',
        'девятитысячные'
      ),
      'сотые',
      'двухсотые',
      'трёхсотые',
      'четырёхсотые',
      'пятисотые',
      'шестисотые',
      'семисотые',
      'восьмисотые',
      'девятисотые'
    ),
    'десятые',
    'двадцатые',
    'тридцатые',
    'сороковые',
    'пятидесятые',
    'шестидесятые',
    'семидесятые',
    'восьмидесятые',
    'девяностые'
  ),
  ('первые', 'одиннадцатые'),
  ('вторые', 'двенадцатые'),
  ('третьи', 'тринадцатые'),
  ('сороковые', 'четырнадцатые'),
  ('пятые', 'пятнадцатые'),
  ('шестые', 'шестнадцатые'),
  ('седьмые', 'семнадцатые'),
  ('восьмые', 'восемнадцатые'),
  ('девятые' 'девятнадцаые')
)
r_mu = (
  (
    (
      (
        'нулевого',
        'тысячного',
        'двухтысячного',
        'трёхтысячного',
        'четырёхтысячного',
        'пятитысячного',
        'шеститысячного',
        'семитысячного',
        'восьмитысячного',
        'девятитысячного'
      ),
      'сотого',
      'двухсотого',
      'трёхсотого',
      'четырёхсотого',
      'пятисотого',
      'шестисотого',
      'семисотого',
      'восьмисотого',
      'девятисотого'
    ),
    'десятого',
    'двадцатого',
    'тридцатого',
    'сорокового',
    'пятидесятого',
    'шестидесятого',
    'семидесятого',
    'восьмидесятого', 
    'девяностого'
  ),
  ('первого', 'одиннадцатого'),
  ('второго', 'двенадцатого'),
  ('третьего', 'тринадцатого'),
  ('четвёртого', 'четырнадцатого'),
  ('пятого', 'пятнадцатого'),
  ('шестого', 'шестнадцатого'),
  ('седьмого', 'семнадцатого'),
  ('восьмого', 'восемнадцатого'),
  ('девятого', 'девятнадцатого')
)
r_zh = (
  (
    (
      (
        'нулевую',
        'тысячную',
        'двухтысячную',
        'трёхтысячную',
        'четырёхтысячную',
        'пятитысячную',
        'шеститысячную',
        'семитысячную',
        'восьмитысячную',
        'девятитысячную'
      ),
      'сотую',
      'двухсотую',
      'трёхсотую',
      'четырёхсотую',
      'пятисотую',
      'шестисотую',
      'семисотую',
      'восьмисотую',
      'девятисотую'
    ),
    'десятую',
    'двадцатую',
    'тридцатую',
    'сороковую',
    'пятидесятую',
    'шестидесятую',
    'семидесятую',
    'восьмидесятую', 
    'девяностую'
  ),
  ('первую', 'одиннадцатую'),
  ('вторую', 'двенадцатую'),
  ('третью', 'тринадцатую'),
  ('четвёртую', 'четырнадцатую'),
  ('пятую', 'пятнадцатую'),
  ('шестую', 'шестнадцатую'),
  ('седьмую', 'семнадцатую'),
  ('восьмую', 'восемнадцатую'),
  ('девятую', 'девятнадцатую')
)
r_mn = (
  (
    (
      (
        'нулевых',
        'тысячных',
        'двухтысячных',
        'трёхтысячных',
        'четырёхтысячных',
        'пятитысячных',
        'шеститысячных',
        'семитысячных',
        'восьмитысячных',
        'девятитысячных'
      ),
      'сотых',
      'двухсотых',
      'трёхсотых',
      'четырёхсотых',
      'пятисотых',
      'шестисотых',
      'семисотых',
      'восьмисотых',
      'девятисотых'
    ),
    'десятых',
    'двадцатых',
    'тридцатых',
    'сороковых',
    'пятидесятых',
    'шестидесятых',
    'семидесятых',
    'восьмидесятых',
    'девяностых'
  ),
  ('первых', 'одиннадцатых'),
  ('вторых', 'двенадцатых'),
  ('третьих', 'тринадцатых'),
  ('сороковых', 'четырнадцатых'),
  ('пятых', 'пятнадцатых'),
  ('шестых', 'шестнадцатых'),
  ('седьмых', 'семнадцатых'),
  ('восьмых', 'восемнадцатых'),
  ('девятых' 'девятнадцатых')
)
d_mu = (
  (
    (
      (
        'нулевому',
        'тысячному',
        'двухтысячному',
        'трёхтысячному',
        'четырёхтысячному',
        'пятитысячному',
        'шеститысячному',
        'семитысячному',
        'восьмитысячному',
        'девятитысячному'
      ),
      'сотому',
      'двухсотому',
      'трёхсотому',
      'четырёхсотому',
      'пятисотому',
      'шестисотому',
      'семисотому',
      'восьмисотому',
      'девятисотому'
    ),
    'десятому',
    'двадцатому',
    'тридцатому',
    'сороковому',
    'пятидесятому',
    'шестидесятому',
    'семидесятому',
    'восьмидесятому', 
    'девяностому'
  ),
  ('первому', 'одиннадцатому'),
  ('второму', 'двенадцатому'),
  ('третьему', 'тринадцатому'),
  ('четвёртому', 'четырнадцатому'),
  ('пятому', 'пятнадцатому'),
  ('шестому', 'шестнадцатому'),
  ('седьмому', 'семнадцатому'),
  ('восьмому', 'восемнадцатому'),
  ('девятому', 'девятнадцатому')
)
d_zh = (
  (
    (
      (
      'нулевой',
      'тысячной',
      'двухтысячной',
      'трёхтысячной',
      'четырёхтысячной',
      'пятитысячной',
      'шеститысячной',
      'семитысячной',
      'восьмитысячной',
      'девятитысячной'
      ),
      'сотой',
      'двухсотой',
      'трёхсотой',
      'четырёхсотой',
      'пятисотой',
      'шестисотой',
      'семисотой',
      'восьмисотой',
      'девятисотой'
    ),
    'десятой',
    'двадцатой',
    'тридцатой',
    'сороковой',
    'пятидесятой',
    'шестидесятой',
    'семидесятой',
    'восьмидесятой', 
    'девяностой'
  ),
  ('первой', 'одиннадцатой'),
  ('второй', 'двенадцатой'),
  ('третью', 'тринадцатой'),
  ('четвёртой', 'четырнадцатой'),
  ('пятой', 'пятнадцатой'),
  ('шестой', 'шестнадцатой'),
  ('седьмой', 'семнадцатой'),
  ('восьмой', 'восемнадцатой'),
  ('девятой', 'девятнадцатой')
)
t_mu = (
  (
    (
      (
        'нулевым',
        'тысячным',
        'двухтысячным',
        'трёхтысячным',
        'четырёхтысячным',
        'пятитысячным',
        'шеститысячным',
        'семитысячным',
        'восьмитысячным',
        'девятитысячным'
      ),
      'сотым',
      'двухсотым',
      'трёхсотым',
      'четырёхсотым',
      'пятисотым',
      'шестисотым',
      'семисотым',
      'восьмисотым',
      'девятисотым'
    ),
    'десятым',
    'двадцатым',
    'тридцатым',
    'сороковым',
    'пятидесятым',
    'шестидесятым',
    'семидесятым',
    'восьмидесятым', 
    'девяностым'
  ),
  ('первым', 'одиннадцатым'),
  ('вторым', 'двенадцатым'),
  ('третьим', 'тринадцатым'),
  ('четвёртым', 'четырнадцатым'),
  ('пятым', 'пятнадцатым'),
  ('шестым', 'шестнадцатым'),
  ('седьмым', 'семнадцатым'),
  ('восьмым', 'восемнадцатым'),
  ('девятым', 'девятнадцатым')
)
t_mn = (
  (
    (
      (
        'нулевыми',
        'тысячными',
        'двухтысячными',
        'трёхтысячными',
        'четырёхтысячными',
        'пятитысячными',
        'шеститысячными',
        'семитысячными',
        'восьмитысячными',
        'девятитысячными'
      ),
      'сотыми',
      'двухсотыми',
      'трёхсотыми',
      'четырёхсотыми',
      'пятисотыми',
      'шестисотыми',
      'семисотыми',
      'восьмисотыми',
      'девятисотыми'
    ),
    'десятыми',
    'двадцатыми',
    'тридцатыми',
    'сороковыми',
    'пятидесятыми',
    'шестидесятыми',
    'семидесятыми',
    'восьмидесятыми',
    'девяностыми'
  ),
  ('первыми', 'одиннадцатым'),
  ('вторыми', 'двенадцатым'),
  ('третьими', 'тринадцатым'),
  ('сороковыми', 'четырнадцатым'),
  ('пятыми', 'пятнадцатым'),
  ('шестыми', 'шестнадцатым'),
  ('седьмым', 'семнадцатым'),
  ('восьмыми', 'восемнадцатым'),
  ('девятыми' 'девятнадцатым')
)
p_mu = (
  (
    (
      (
        'нулевом',
        'тысячном',
        'двухтысячном',
        'трёхтысячном',
        'четырёхтысячном',
        'пятитысячном',
        'шеститысячном',
        'семитысячном',
        'восьмитысячном',
        'девятитысячном'
      ),
      'сотом',
      'двухсотом',
      'трёхсотом',
      'четырёхсотом',
      'пятисотом',
      'шестисотом',
      'семисотом',
      'восьмисотом',
      'девятисотом'
    ),
    'десятом',
    'двадцатом',
    'тридцатом',
    'сороковом',
    'пятидесятом',
    'шестидесятом',
    'семидесятом',
    'восьмидесятом', 
    'девяностом'
  ),
  ('первом', 'одиннадцатом'),
  ('втором', 'двенадцатом'),
  ('третьем', 'тринадцатом'),
  ('четвёртом', 'четырнадцатом'),
  ('пятом', 'пятнадцатом'),
  ('шестом', 'шестнадцатом'),
  ('седьмом', 'семнадцатом'),
  ('восьмом', 'восемнадцатом'),
  ('девятом', 'девятнадцатом')
)

# Сопоставление остальных форм
r_sr = r_mu
d_sr = d_mu
d_mn = t_mu
v_zh = r_zh
t_sr = t_mu
t_zh = r_zh
p_sr = p_mu
p_zh = r_zh
p_mn = r_mn

# Формы единиц измерения
# Единственное число/форма для чисел, оканчивающихся на 2,3,4/множественное число/форма для дробей
forms = {
    '%': ('процент', 'процента', 'процентов', 'процента'),
    '°': ('градус', 'градуса', 'градусов', 'градуса'),
    '℃': ('градус Цельсия', 'градуса Цельсия', 'градусов Цельсия', 'градуса Цельсия'),
    '$': ('доллар', 'доллара', 'долларов', 'доллара'),
    'кг': ('килограмм', 'килограмма', 'килограммов', 'килограмма'),
    'км': ('километр', 'километра', 'километров', 'километра'),
    'мг': ('миллиграмм', 'миллиграмма', 'миллиграммов', 'миллиграмма'),
    'мм': ('миллиметр', 'миллиметра', 'миллиметров', 'миллиметра'),
    'см': ('сантиметр', 'сантиметра', 'сантиметров', 'сантиметра'),
    'м': ('метр', 'метра', 'метров', 'метра'),
    'т': ('тонна', 'тонны', 'тонн', 'тонны'),
    'кВт': ('киловатт', 'киловатта', 'киловатт', 'киловатта'),
    'МВт': ('мегаватт', 'мегаватта', 'мегаватт', 'мегаватта'),
    'ГВт': ('гигаватт', 'гигаватта', 'гигаватт', 'гигаватта'),
    'Вт': ('ватт', 'ватта', 'ватт', 'ватта'),
    '₽': ('рубль', 'рубля', 'рублей', 'рубля'),
    '£': ('фунт стерлингов', 'фунта стерлингов', 'фунтов стерлингов', 'фунта стерлингов'),
    'л\u002Eс\u002E': ('лошадиная сила', 'лошадиных силы', 'лошадиных сил', 'лошадиной силы'),
    'тыс\u002E': ('тысяча', 'тысячи', 'тысяч', 'тысячи'),
    'млн': ('миллион', 'миллиона', 'миллионов', 'миллиона'),
    'млрд': ('миллиард', 'миллиарда', 'миллиардов', 'миллиарда'),
    'трлн': ('триллион', 'триллиона', 'триллионов', 'триллиона')
}

# Определение Римских цифр
values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def ordinal(num, casus):
    if num[-1] == '0':
        try:
            if num[-2] == '0':
                if num[-3] == '0':
                    prenum = ''
                    number = casus[0][0][0][int(num[-4])]
                else:
                    if len(num) == 3:
                        prenum = ''
                    else:
                        prenum = num[:-3] + '000 '
                    number = casus[0][0][int(num[-3])]
            else:
                if len(num) == 2:
                    prenum = ''
                else:
                    prenum = num[:-2]
                    if int(prenum) == 0:
                        prenum += ' '
                    else:
                        prenum += '00 '
                number = casus[0][int(num[-2])]
        except:
            prenum = ''
            number = casus[0][0][0][0]
    else:
        if len(num) == 1:
            prenum = ''
            dec = 0
        else:
            if num[-2] == '1':
                dec = 1
                if len(num) == 2:
                    prenum = ''
                else:
                    prenum = num[:-2]
                    if int(prenum) == 0:
                        prenum += ' '
                    else:
                        prenum += '00 '
            else:
                prenum = num[:-1]
                if int(prenum) == 0:
                    prenum += ' '
                else:
                    prenum += '0 '
                dec = 0
        number = casus[int(num[-1])][dec]
    return prenum + number

# Перевод римских чисел в арабские
# Код заимствован (с изменениями) у Jeff Wheeler
# FIXME как быть например с английскими словами: "I"-"Я" или "ID"-"АйДи"
def roman2arabic(value):
    total = 0
    prevValue = 0
    value = value[::-1]
    for char in value:
        if values[char] >= prevValue:
            total += values[char]
        else:
            total -= values[char]
        prevValue = values[char]
    total = str(total)
    return total

def substant(num, key):
    if len(num) > 1 and num[-2] == '1':
        form = forms[key][2]
    else:
        if num[-1] =='1':
            form = forms[key][0]
        elif 1 < int(num[-1]) < 5:
            form = forms[key][1]
        else:
            form = forms[key][2]
    return form

def feminin(num):
    num = str(int(num))
    if len(num) == 1:
        if num == '1':
            num = 'одна'
        elif num == '2':
            num = 'две'
    else:
        if num[-2] != '1':
            if num[-1] == '1':
                num = num[:-1] + '0 одна'
            elif num[-1] == '2':
                num = num[:-1] + '0 две'
    return num

# =================================
# Основная функция обработки текста
# =================================

def txt_prep(text):

    ##  ШАБЛОНЫ  ##

    text = sub(r'\+ ?', 'плюс ', text)
    text = sub(r'(?<!\w)-(?=\d)', 'минус ', text)
    text = sub(r'[ \t]{2,}', ' ', text)
    text = sub(r' +(\n|\Z)', r'\1', text)
    text = sub(r'\n{2,}', r'\n', text)
    text = sub(r'[«»"]', '', text)
    text = sub(r'[‑–−—]', '-', text)

    text = sub(r'№ ?', 'номер ', text)
    text = sub(r'\b[Тт]\. ?е\.', 'то есть', text)
    text = sub(r' т\. ?д\.', ' так далее', text)
    text = sub(r' т\. ?п\.', ' тому подобное', text)
    text = sub(r' н\. ?э\.', ' нашей эры', text)
    text = sub(r'\b[Пп]рим\. ред\.', 'примечание редактора', text)
    text = sub(r'\b[Рр]ед\.', 'редактор', text)
    text = sub(r'\b[Пп]рим\.', 'примечание', text)

    text = sub(r'\b([Гг])-(н|на|не|ном|ну)\b', r'\1осподи\2', text)
    text = sub(r'\b([Гг])-(жа|же|жи|жой|жу)\b', r'\1оспо\2', text)

    text = sub(r' ?± ?', ' плюс-минус ', text)
    text = sub(r' ?= ?', ' равно ', text)
    text = sub(r' ?≈ ?', ' приближённо равно ', text)

    # Единицы измерения и денежные единицы

    text = sub(r'\bруб\.', '₽', text)
    text = sub(r'(\$|€|£|₽)([0-9,]+)', r'\2\1', text)
    text = sub(r'(\$|€|£|₽) ?(тыс\.|млн|млрд|трлн|тысяч[аи]?|миллион[аов]{,2}|миллиард[аов]{,2}|триллион[аов]{,2})', r' \2 \1', text)
    text = sub(' ?€', ' евро', text)

    units = r'(%|°|℃|£|₽|\$|кг|км|мг|мм|м\b|см\b|т\b|кВт|МВт|ГВт|Вт|л\u002Eс\u002E|тыс\u002E|млн|млрд|трлн)'
    text = sub(r'(?<=\d) ?' + units,  r'\1', text)

    samples = findall(r'(\d+,\d+)' + units, text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], sample[0] + ' ' + forms[sample[1]][3], 1)
    samples = findall(r'(\d+)' + units, text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], sample[0] + ' ' + substant(sample[0], sample[1]), 1)
    samples = findall(r'(тысяч[аи]?|миллион[аов]{,2}|миллиард[аов]{,2}|триллион[аов]{,2}) ?' + units, text)
    for sample in samples:
        text = text.replace(sample[0] + ' ' + sample[1], sample[0] + ' ' + forms[sample[1]][2], 1)

    text = sub(r'/(сек|с)\b', r' в секунду', text)
    text = sub(r'/(час|ч)\b', r' в час', text)

    # Удаление пробелов между разрядами /только целая часть числа/
    text = sub(r'(?<=\d) (?=\d{3})', r'', text)

    # Десятичные дроби (до тысячных включительно)
    samples = findall(r'(\d+,)(\d{1,3})\b', text)
    for sample in samples:
        length = len(sample[1])
        full = feminin(sample[0][0:-1])
        if full[-1] == 'а':
            full += ' целая '
        else:
            full += ' целых '
        if length == 1:
            frac = ' десят'
        elif length == 2:
            frac = ' сот'
        else:
            frac = ' тысячн'
        decimal = feminin(sample[1])
        if decimal[-1] == 'а':
            frac += 'ая'
        else:
            frac += 'ых'
        text = text.replace(sample[0] + sample[1],  full + 'и ' + decimal + frac, 1)

    # Проверка должна следовать после обработки десятичных дробей
    samples = findall(r'(\d+) (минут[аы]?|недел[иья]|секунд[аы]?|тонн[аы]|тысяч[аи]?|лошадин[аеыя]{2} сил[аы]?)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + ' ' + sample[1], feminin(sample[0]) + ' ' + sample[1], 1)

    # Римские цифры
    roman = findall(r'\b[IVXLCDM]+\b', text)
    for i in roman:
        text = text.replace(i, roman2arabic(i), 1)
    
    text = sub(r'(\d)( ранга)\b', r'\1-го\2', text)
    text = sub(r'(\d+)( Олимпийски)([еимх]{1,2})', r'\1-\3\2\3', text)
    
    # Даты
    
    text = sub(r'(\d) - (\d)', r'\1-\2', text)
    text = sub(r'(?<=\d)(г\.|гг\.)', r' \1', text)
    
    text = sub(r'(январ[еюьям]{1,2}|феврал[еюьям]{1,2}|март[аеуом]{0,2}|апрел[еюьям]{1,2}|ма[йюяем]{1,2}|июн[еюьям]{1,2}|июл[еюьям]{1,2}|август[аеуом]{0,2}|сентябр[еюьям]{1,2}|октябр[еюьям]{1,2}|ноябр[еюьям]{1,2}|декабр[еюьям]{1,2}|начал[аеому]{1,2}|середин[аеойуы]{1,2}|кон[ецауом]{2,3}|половин[аеуыой]{1,2}|лет[ауом]{1,2}|весн[аеуыой]{1,2}|осен[иью]{1,2})( \d+) (года\b|г\.)', r'\1\2-го года', text)
    
    text = sub(r'([Пп]еред \d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1-м \2', text)
    
    text = sub(r'\b([Зз]а|[Нн]а|[Пп]о)( \d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1\2-е \3', text)
    text = sub(r'\b([Дд]о|[Пп]осле|[Сс]о?)( \d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1\2-го \3', text)
    text = sub(r'\b([Кк]о?)( \d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1\2-му \3', text)
    text = sub(r'(\d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1-го \2', text)
    
    text = sub(r'(начал[аеому]{1,2}|середин[аеойуы]{1,2}|кон[ецауом]{2,3}|половин[аеуыой]{1,2})( \d+) гг\.', r'\1\2-х годов', text)
    
    text = sub(r'(ноч[иь] со? \d+)( на \d+)', r'\1-го\2', text)
    
    text = sub(r'(\d+) годов', r'\1-го годов', text)
    text = sub(r'\b([Кк] \d+)-(\d+) (годам|гг\.)', r'\1-му \2-му годам', text)
    text = sub(r'(\d+-м )(гг\.)', r'\1годам', text)
    
    text = sub(r'\b(\d+) века\b', r'\1-го века', text) # Спорный шаблон
    text = sub(r'\b([Вв] \d+) (веке|в\.)', r'\1-м веке', text)
    text = sub(r'\b([Кк] \d+)(-му) (веку|в\.)', r'\1-му веку', text)
    text = sub(r'\b([Дд]о|[Пп]осле|[Сс])( \d+) (века|в\.)', r'\1\2-го века', text)
    text = sub(r'\b([Вв] \d+)-(\d+) (веках|вв\.)', r'\1-м \2-м веках', text)
    text = sub(r'\b([Кк] \d+)-(\d+) векам', r'\1-му \2-му векам', text)
    
    text = sub(r'\b([Вв] \d+) (году|г\.)', r'\1-м году', text)
    text = sub(r'\b([Кк] \d+) (году|г\.)', r'\1-му году', text)
    
    text = sub(r'([Пп]о сравнению с|[Пп]еред)( \d+) г\.', r'\1\2-м годом', text)
    text = sub(r'(\d+) годом', r'\1-м годом', text)
    text = sub(r'\b([Дд]о|[Пп]осле|[Сс])( \d+) (года|г\.)', r'\1\2-го года', text)
    
    text = sub(r'\b([Вв] \d+)-(\d+) (годах|гг\.)', r'\1-м \2-м годах', text)
    text = sub(r'(\d+)-(\d+) (годы|гг\.)', r'\1-й \2-й годы', text)
    text = sub(r'(\d+) (или|и) (\d+) (годы|гг\.)', r'\1-й \2 \3-й годы', text)
    
    text = sub(r'\b([Вв] \d+) (годах|гг\.)', r'\1-х годах', text)
    text = sub(r'\b([Дд]о|[Пп]осле|[Сс])( \d+) (годов|гг\.)', r'\1\2-х годов', text)
    text = sub(r'\b([Сс] \d+) по (\d+) (годы|гг\.)', r'\1-го по \2-й годы', text)
    
    text = sub(r'([Зз]им[аеойуы]{1,2} \d+)-(\d+)', r'\1-го \2-го', text)
    
    text = sub(r'(\d)( квартал)\b', r'\1-й\2', text)
    text = sub(r'(\d)( квартала)\b', r'\1-го\2', text)
    text = sub(r'(\d)( кварталу)\b', r'\1-му\2', text)
    text = sub(r'(\d)( квартал)(е|ом)\b', r'\1-м\2\3', text)
    
    text = sub(r'\b([Дд]о|[Кк]о?||[Пп]осле|[Сс]о?)( \d+)( недел)(е|ей|и)\b', r'\1\2-й\3\4', text)
    
    text = sub(r'(\d+-го )г\.', r'\1года', text)
    text = sub(r'([Сс] \d+-м )г\.', r'\1годом', text)
    text = sub(r'(\d+-е )гг\.', r'\1годы', text)
    text = sub(r'(\d+-ми )гг\.', r'\1годами', text)
    text = sub(r'(\d+-х )гг\.', r'\1годов', text)
    
    text = sub(r'\b(\d+)-(\d+)-(го|ми|х)\b', r'\1-\3 \2-\3', text)
    
    text = sub(r'(1\d|[02-9][05-9]|\b[5-9]) года\b', r'\1-го года', text)
    text = sub(r'(1\d|[02-9][02-9]|\b[2-9]) год\b', r'\1-й год', text)
    text = sub(r'(\d+) г\.', r'\1-й год', text)
    
    text = sub(r'(\d+) г\.р\.', r'\1-го года рождения', text)
    
    text = sub(r'(\d+)-(\d+) (тысяче|сто)летия\b', r'\1-е \2-е \3летия\b', text)
    text = sub(r'\b([Сс]о?)( \d+)( по \d+) (тысяче|сто)летие', r'\1\2-го\3-е \4летие', text)
    text = sub(r'\b([Вв]о?)( \d+)-(\d+) (тысяче|сто)летиях', r'\1\2-м \3-м \4летиях', text)
    text = sub(r'(\d+) (тысяче|сто)летие', r'\1-е \2летие', text)
    text = sub(r'(\d+) (тысяче|сто)летия\b', r'\1-го \2летия', text)
    text = sub(r'(\d+) (тысяче|сто)летию', r'\1-му \2летию', text)
    text = sub(r'(\d+) (тысяче|сто)летии', r'\1-м \2летии', text)
    
    # Порядковые числительные
    
    samples = findall(r'(\d+0)(-\d+0-е годы)', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], ordinal(sample[0], i_mn) + sample[1], 1)
    
    samples = findall(r'(\d+-е)( Олимпийские| годы)', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], ordinal(sample[0][:-2], i_mn) + sample[1], 1)
    
    samples = findall(r'([Вв] )(\d{,}0-е)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], i_mn), 1)
    
    samples = findall(r'(\d+0)(-\d+0-м годам)', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], ordinal(sample[0], d_mn) + sample[1], 1)
    
    samples = findall(r'([Кк] )(\d+-м)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], d_mn), 1)
    
    samples = findall(r'(\d+-х-)', text)
    for sample in samples:
        text = text.replace(sample, ordinal(sample[:-3], r_mnoz) + ' ', 1)
    
    samples = findall(r'\d+-я\b', text)
    for sample in samples:
        text = text.replace(sample, ordinal(sample[:-2], i_zh), 1)
    
    samples = findall(r'\b([Вв]о? |[Нн]а )(\d+-ю)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], r_zh), 1)
    
    samples = findall(r'\d+-ю\b', text)
    for sample in samples:
        text = text.replace(sample, ordinal(sample[:-2], r_zh), 1)
    
    samples = findall(r'\b([Вв] |[Нн]а |[Пп]ри )(\d+-м)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], p_mu), 1)
    
    samples = findall(r'\b([Кк] )(\d+-м)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], d_mn), 1)
    
    samples = findall(r'\b([Сс] )(\d+-м)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], t_mu), 1)
    
    samples = findall(r'\d+-му\b', text)
    for sample in samples:
        text = text.replace(sample, ordinal(sample[:-3], d_mu), 1)
    
    samples = findall(r'\d+-го\b', text)
    for sample in samples:
        text = text.replace(sample, ordinal(sample[:-3], r_mu), 1)
    
    samples = findall(r'\d+-ми\b', text)
    for sample in samples:
        text = text.replace(sample, ordinal(sample[:-3], t_mn), 1)
    
    samples = findall(r'(\d{,}1\d|\d{,}[02-9][015-9]|[015-9])-х\b', text)
    for sample in samples:
        text = text.replace(sample + '-х', ordinal(sample, r_mn), 1)
    
    samples = findall(r'\b([Дд]о|[Пп]осле|[Сс]о?) (\d+-й)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + ' ' + sample[1], sample[0] + ' ' + ordinal(sample[1][:-2], r_zh), 1)
    
    samples = findall(r'\d+-й\b', text)
    for sample in samples:
        text = text.replace(sample, ordinal(sample[:-2], i_mu), 1)
    
    samples = findall(r'(\d+-м )(годах|веках|(сто|тысяче)летиях)\b', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], ordinal(sample[0][:-3], p_mu) + ' ' + sample[1], 1)
    
    samples = findall(r'(\d+-м)( [а-яА-Я]+м\b)', text)
    for sample in samples:
        text = text.replace(sample[0] + sample[1], ordinal(sample[0][:-2], t_mu) + sample[1], 1)
    
    samples = findall(r'\d+-е\b', text)
    for sample in samples:
        text = text.replace(sample, ordinal(sample[:-2], i_sr), 1)

    # Буквы греческого алфавита
    greekletters = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσΤτΥυΦφΧχΨψΩως'
    letternames = ('альфа', 'бета', 'гамма', 'дельта', 'эпсилон', 'дзета', 'эта', 'тета', 'йота', 'каппа', 'лямбда', 'мю', 'ню', 'кси', 'омикрон', 'пи', 'ро', 'сигма', 'тау', 'ипсилон', 'фи', 'хи', 'пси', 'омега', 'сигма')
    for j in greekletters:
        text = text.replace(j, letternames[greekletters.index(j)//2])

    text = sub(r'(\w)(\n|\Z)', r'\1.\2', text)

    return text
