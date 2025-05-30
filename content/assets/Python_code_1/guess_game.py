# 終極密碼戰(while 迴圈應用)

from random import randint

pwd = randint(1, 100) # 隨機產生一個 1 ~ 100 間的數字作為密碼。
L = 1
R = 100
c = 0 # 用以紀錄猜測次數。

# 因不確定需要猜測多少次才能猜中密碼，因此使用 while迴圈。
while True:
	print('密碼介於 %d 至 %d 之間。' %(L, R))
	guess = int(input('輸入密碼：'))
	c += 1

	print()
	if guess < L or guess > R:
		print('Invalid Input.\nPlease Try Again.\n')
	elif guess == pwd:
		print('密碼正確！\n密碼為：%d' %(pwd), end = '')
		break # 遊戲終止
	elif guess > pwd:
		R = guess - 1
	else:
		L = guess + 1

print('，共猜了 %d 次。' %(c))
