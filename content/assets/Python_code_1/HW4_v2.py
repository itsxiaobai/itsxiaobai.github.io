print('\n100 ~ 10,000,000 之間的水仙花數有：')
i = 100
c = 0
while i <= 10000000:
	n = i
	d = 0

	while n > 0:
		n //= 10
		d += 1

	n = i
	SUM = 0
	while n > 0:
		SUM += (n % 10)**d
		n //= 10

	if SUM == i:
		print(i, end = ' ')
		c += 1

	i += 1

print('共 %d 個。\n'%(c))
