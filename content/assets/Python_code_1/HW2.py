spend = int(input('輸入消費金額(NTD)：'))

if spend <= 0:
	print('\nError Input.\n消費金額不可小於或等於零。')
elif spend < 3000:
	print('\n無消費優惠。\n實付金額：NTD$ %d 元。'%(spend))
elif spend < 5000:
	print('\n9折優惠。\n實付金額：NTD$ %d 元。'%(spend * 0.9))
elif spend < 10000:
	print('\n85折優惠，減200。\n實付金額：NTD$ %d 元。'%(spend * 0.85 - 200))
elif spend < 20000:
	print('\n8折優惠，減500。\n實付金額：NTD$ %d 元。'%(spend * 0.8 - 500))
elif spend < 30000:
	print('\n75折優惠，減1000。\n實付金額：NTD$ %d 元。'%(spend * 0.75 - 1000))
else:
	print('\n7折優惠，減1500。\n實付金額：NTD$ %d 元。'%(spend * 0.7 - 1500))
