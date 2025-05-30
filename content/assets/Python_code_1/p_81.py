# 求最大公因數，使用輾轉相除法

x = int(input('輸入正整數一：'))
y = int(input('輸入正整數二：'))

while y > 0:
	z = x % y
	x = y
	y = z

print('最大公因數(GCD)：%d'%(x))
