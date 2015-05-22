#!-*-coding:utf-8-*-

import pymorphy2
p = morph = pymorphy2.MorphAnalyzer()
print(morph.parse('люди'))
