pi = 0
for i in range(1, 1001):
	t = 4 / (2 * i - 1)

	if i % 2 != 0:
		pi += t
	else:
		pi -= t

print('\npi =', pi)
