# break 與 continue 敘述

# 1 2 3 4 5 6 7 8 9 10
for i in range(1, 11):
	print(i, end = ' ')


print()


# 1 3 5 7 9
for i in range(1, 11):
	if i % 2 == 0:
		continue
	print(i, end = ' ')


print()


# 1
for i in range(1, 11):
	if i % 2 == 0:
		break
	print(i, end = ' ')


