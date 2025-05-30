# 「連續」輸入五筆成績，計算總分和平均。

SUM = 0
for i in range(5):
	s = int(input('輸入 %d 號成績：'%(i + 1)))
	SUM += s

print('\n總分 = %d\n平均 = %.1f'%(SUM, SUM / 5))
