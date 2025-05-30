s = int(input('成績\n'))

if s > 100 or s < 0:
    print('Error\n')

elif s >= 90:
    print('優\n')

elif s >= 80:
    print('甲\n')

elif s >= 70:
    print('乙\n')

elif s >= 60:
    print('丙\n')

else:
    print('丁\n')


'''
if s >= 90:
    print('優\n')

elif s >= 70 and s < 80:
    print('乙\n')

elif s >= 80 and s < 90:
    print('甲\n')

elif s >= 60 and s < 70:
    print('丙\n')

else:
    print('丁\n')
'''

'''
if s >= 60 and s < 70:
    print('丙\n')

elif s >= 70 and s < 80:
    print('乙\n')

elif s < 60:
    print('丁\n')

elif s >= 90:
    print('優\n')

else:
    print('甲\n')
'''