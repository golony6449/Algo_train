value=int(raw_input())
count=0
for k in range(1,value+1):
    if k<100:
        count=count+1
    elif k<1000:
        b=k/100%10
        c=k/10%10
        d=k%10
#        print b,c,d,k
        if abs(b-c)==abs(c-d) and abs(b-c)==abs(b-d)/2:
            count=count+1
            #print k
    elif k==1000:
        pass
print count
