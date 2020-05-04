'''input
4
1 10 100
10000000000000000 10000000000000000 10000000000000000
23 34 45
1 2 5
'''
q = int(input())
for Q in range(q):
	l = list(map(int,input().split()))
	l.sort()
	a = l[1]
	b = l[0]
	c = l[2]
	tempb = b
	b+=(a-b)
	c-=(a-tempb)
	c=c//2
	print(a+c)