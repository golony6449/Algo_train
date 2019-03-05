time=int(input())
contain=[]

for a in range(time):
    para=input().split()
    length=len(contain)
    
    if para[0]=='push':
        contain.append(int(para[1]))
        
    elif para[0]=='pop':
        if length==0:
            print (-1)
        else:
            print (contain[length-1])
            contain.remove(contain[length-1])
            
    elif para[0]=='size':
        print (length)
        
    elif para[0]=='empty':
        if length==0:
            print(1)
        else:
            print(0)
            
    elif para[0]=='top':
        if length==0:
            print(-1)
        else:
            print (contain[length-1])
    else:
        continue
    print(contain)
