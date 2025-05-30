# 複利計算

p = float(input('本金：'))
r = float(input('年利率(%)：'))
e = int(input('目標金額：'))
y = 0

# 因無法準確預估達到目標金額需要存多少年，所以使用 while 迴圈。
while p < e:
	p *= (1 + r / 100)
	y += 1

print('\n存 %d 年後，本利和為 %d 元。\n'%(y, p))
