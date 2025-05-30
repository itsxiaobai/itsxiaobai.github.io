'''
雙向選擇結構 Bi-Selection Structure

if condition:
	statement 1
else:
	statement 2

如條件為真，則執行敘述1。
反之，條件為假，則執行敘述2。
'''

# 範例：課本 p.064 圖2-3.1。
s = input('外面下雨？')

if s == 'Y' or s == 'y':
	print('在家裡玩Game\n')
else:
	print('去公園玩\n')


# 範例：奇偶數判斷
n = int(input('輸入任一整數：'))

if n % 2 == 0:
	print('%d 為偶數。'%(n))
else:
	print('%d 為奇數。'%(n))

