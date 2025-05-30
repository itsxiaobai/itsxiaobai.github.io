# 雙重迴圈(巢狀迴圈)

# 列印 *
print('*')

print()

# 列印 *****
for i in range(5):
	print('*', end = '')

print('\n')

'''
*****
*****
*****
*****
*****
'''
for i in range(5):
	for j in range(5):
		print('*', end = '')
	print()

print()

'''
*
**
***
****
*****
'''
for i in range(5):
	for j in range(i + 1):
		print('*', end = '')
	print()

print()

'''
*****
****
***
**
*
'''
for i in range(5):
	for j in range(5 - i):
		print('*', end = '')
	print()

print()

'''
*****
 ****
  ***
   **
    *
'''
for i in range(5):
	for k in range(i):
		print(' ', end = '')
	for j in range(5 - i):
		print('*', end = '')
	print()

print()

'''
    *
   **
  ***
 ****
*****
'''
for i in range(5):
	for k in range(4 - i):
		print(' ', end = '')
	for j in range(i + 1):
		print('*', end = '')
	print()

print()

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(5):
	for k in range(4 - i):
		print(' ', end = '')
	for j in range(2 * i + 1):
		print('*', end = '')
	print()

print()

'''
*****
*****
**@**
*****
*****
'''
for i in range(5):
	for j in range(5):
		if i == 2 and j == 2:
			print('@', end = '')
		else:
			print('*', end = '')
	print()

print()
