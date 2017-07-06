value=raw_input().split()
time=int(value[0])
money=int(value[1])
coin=[]
count=0

for time in range(time):
    coin.insert(0,int(raw_input()))
for k in coin:
    temp=money/k
    if temp==0:
        pass
    else:
        count=count+temp
        money=money-temp*k
print count
