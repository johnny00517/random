
import random
start = input('請輸入開始值:  ')
end = input('請輸入結束值:  ')
start = int(start)
end = int(end)

r = random.randint(start , end)
print ('答案:', r)
count = 0
c = count

while True:
	c =c + 1
	
	x = input('請輸入數字:  ')
	x = int(x)
	if x == r:
		print('猜對了')
		break
	else:
		if x > r:
			print('比答案大')
		if x < r:
			print('比答案小')

	print ('這是第', c , '次')
