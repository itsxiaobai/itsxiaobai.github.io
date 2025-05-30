'''
數字倒轉
如：93712 -> 21739
'''

# Method 1
n = int(input('輸入正整數：'))

print('反轉：', end = '')
while n > 0:
	print(n % 10, end = '')
	n = n // 10
print()


# Method 2
'''
n = int(input('輸入正整數：'))
r = 0

while n > 0:
	r = r * 10 + n % 10
	n = n // 10

print('反轉：%d'%(r))
'''
