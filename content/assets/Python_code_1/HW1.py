r = float(input('\n圓柱體半徑(cm)：'))
h = float(input('圓柱體高(cm)：'))

print('\n表面積 = "%.2f" 平方公分'%(2 * 3.14 * r * (r + h)))
print('體積 = "%.2f" 立方公分'%(3.14 * r**2 * h))
