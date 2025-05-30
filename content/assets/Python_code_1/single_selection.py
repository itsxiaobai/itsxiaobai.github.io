'''
單一選擇結構 Single-Selection Structure

if condition:
	statement

如條件為真，則執行敘述。
反之，條件為假，則忽略敘述。
'''

# 範例：成績系統 59分自動加 1分。
s = int(input('輸入成績：'))

if s == 59:
	s += 1

print('最後成績：%d\n'%(s))


# 範例：成績系統 59分自動加 1分；58分自動加 2分。
s = int(input('輸入成績：'))

if s == 59:
	s += 1

if s == 58:
	s += 2

'''
if s == 58 or s == 59:
	s = 60
'''

print('最後成績：%d\n'%(s))
