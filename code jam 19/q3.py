def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
	
no = int(input())

for h in range(no):

	lar,leng=list(map(int,input().split()))
	st=list(map(int,input().split()))
	seed=gcd(st[0],st[1])
	alph=set([])
	alph.add(st[0]//seed)
	alph.add(seed)
	for i in range(1,leng):
		alph.add(st[i]//seed)
		seed=st[i]//seed
	alph=list(alph)
	alph.sort()

	final=chr(65+alph.index(st[0]/gcd(st[0],st[1])))
	for i in range(leng-1):
		final+=chr(65+alph.index(gcd(st[i],st[i+1])))
	final+=chr(65+alph.index(st[-1]/gcd(st[-1],st[-2])))

	print('Case #'+str(h+1)+': '+final)
