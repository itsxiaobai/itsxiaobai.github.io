# 九九乘法表

'''
2 * 1 = 2	2 * 2 = 4	...	2 * 9 = 18
...
9 * 1 = 9	9 * 2 = 18	...	9 * 9 = 81
'''
for i in range(2, 10):
	for j in range(1, 10):
		print('%d * %d = %d'%(i, j, i * j), end = '\t')
	print()

print('\n=========\n')

'''
2 * 1 = 2	3 * 1 = 3	...	9 * 1 = 9
...
2 * 9 = 18	3 * 9 = 27	...	9 * 9 = 81
'''
for j in range(1, 10):
	for i in range(2, 10):
		print('%d * %d = %d'%(i, j, i * j), end = '\t')
	print()
