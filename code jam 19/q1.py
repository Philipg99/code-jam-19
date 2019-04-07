no = int(input())

for t in range(no):
    num = list(map(int,list(input())))
    clone=[0]*len(num)
    for i in range(len(num)):
        if num[i]==4:
            num[i]=3
            clone[i]=1
                
    s1=''
    for i in num:
        s1+=str(i)
    s2=''
    for i in clone:
        s2+=str(i)
    
    print('Case #'+str(t+1)+' '+str(int(s1))+' '+str(int(s2)))
