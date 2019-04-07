def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
	
no = int(input())

for h in range(no):

	lar,leng=list(map(int,input().split()))
	st=list(map(int,input().split()))

	let=[st[0]/gcd(st[0],st[1])]
	for i in range(leng):
		let+=[st[i]/let[-1]]

	alph=[]
	for i in let:
	    if i not in alph:
	        alph+=[i]
	alph.sort()

	final=''
	for i in let:
		final+=chr(alph.index(i)+65)
	print('Case #'+str(h+1)+': '+final)
