'''
多向選擇結構 Multi-Selection Structure

if condition 1:
	statement 1
elif condition 2:
	statement 2
else:
	statement 3

如條件1為真，則執行敘述1。
如條件1為假，則檢查條件2是否為真。
如條件2為真，則執行敘述2。
如條件2為假，則執行敘述3。
'''


# 範例：成績等第轉換
s = int(input('輸入分數：'))

if s >= 90:
	print('等第：優等\n')
elif s >= 80:
	print('等第：甲等\n')
elif s >= 70:
	print('等第：乙等\n')	
elif s >= 60:
	print('等第：丙等\n')
else:
	print('等第：丁等\n')


print('')


# 範例：購物優惠計算
'''
消費滿 5,000，打九折。
消費滿 10,000，打八五折。
消費滿 20,000，打八折。
消費滿 30,000，打七五折。
'''

m = int('輸入消費金額：')

if m < 5000:
	print('Pay = %d'%(s))
elif m < 10000:
	print('Pay = %d'%(s * 0.9))
elif m < 20000:
	print('Pay = %d'%(s * 0.85))
elif m < 30000:
	print('Pay = %d'%(s * 0.8))
else:
	print('Pay = %d'%(s * 0.75))


'''
from math import floor, ceil
x = 1.99

四捨五入：round(x)	->	2
無條件捨去：floor(x)	->	1
無條件進位：ceil(x)	->	2

'''
