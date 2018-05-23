#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# список списков слов мужского рода в формате:
# (
#  (                    # единственное число
#    1. именительный,
#    2. родительный,
#    3. дательный,
#    4. винительный,
#    5. творительный,
#    6. предложный,
#  ),
#  (                    # множественное число
#    1. именительный,
#    2. родительный,
#    3. дательный,
#    4. винительный,
#    5. творительный,
#    6. предложный,
#  )
# )
words = (
         (('', 'автобуса', '', '', 'автобусом', 'автобусе'),
          ('', 'автобусов', '', '', '', '')),

         (('', 'автомата', '', '', 'автоматом', 'автомате'),
          ('', 'автоматов', '', '', '', '')),

         (('', 'автомобиля', '', '', 'автомобилем', 'автомобиле'),
          ('', 'автомобилей', '', '', '', '')),

         (('', 'автора', '', 'автора', 'автором', 'авторе'),
          ('', 'авторов', '', 'авторов', '', '')),
        )
