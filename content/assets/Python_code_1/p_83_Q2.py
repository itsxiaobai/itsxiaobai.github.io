# Textbook p.83 演練實作 Question 2

s = int(input('Enter the score: '))

if s < 0 or s > 100:
	print('Invalid Input.')
elif s < 80:
	print('Reward: $%d'%(0))
elif s <= 90:
	print('Reward: $%d'%(100))
elif s < 98:
	print('Reward: $%d'%(100 + (s - 90) * 2))
else:
	print('Reward: $%d'%(100 + (97 - 90) * 2 + (s - 97) * 5))
