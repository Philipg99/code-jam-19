no = int(input())

for h in range(no):
    si =  int(input())
    seq =  input()
    cor=''
    for i in seq:
        if i == 'S':
            cor+='E'
        else:
            cor+='S'
            
    print('Case #'+str(h+1)+': '+cor)
