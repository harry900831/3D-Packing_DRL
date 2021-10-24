import numpy as np
import random as rd



n = int(input())
mxval = 5


testdata = []
cnt = 0
while n > 0 : 
	num = rd.randint(1, n)
	num = rd.randint(1, num)
	x = rd.randint(1, mxval);
	y = rd.randint(1, mxval);
	z = rd.randint(1, mxval);
	for i in range(num) : testdata.append([x, y, z, cnt]);
	n -= num
	cnt+=1

print(testdata)
np.save('testdata', x)







