'''
s = int(input('輸入金額：\n'))

if s < 5000:
    print(s)

elif s < 10000:
    print(round(s * 0.9)) # round(想要算的數字,到小數點第幾位)

elif s < 20000:
    print(round(s * 0.85))

elif s < 30000:
    print(round(s * 0.8))

else:
    print(round(s * 0.75))
'''

'''
from math import floor # floor : 無條件捨去小數點

print(floor(1999999.30))

from math import ceil # ceil : 無條件進位小數點
print(ceil(169999.03)) 
'''

s = int(input('輸入金額：\n'))

if s < 5000:
    print(s)

elif s < 10000:
    print(round(s * 0.9)) # round(想要算的數字,到小數點第幾位)

elif s < 20000:
    print(round(s * 0.85))

elif s < 30000:
    print(round(s * 0.8))

else:
    print(round(s * 0.75))

