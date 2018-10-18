# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for sub in points:
    sum = sum + points[sub]
print(int(sum))