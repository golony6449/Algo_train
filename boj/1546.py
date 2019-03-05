count=int(raw_input())
value=raw_input().split()
max=0
for i in value:
    if int(i)>max:
        max=int(i)
total=0.0
for j in value:
    total=total+float(j)/max*100
average=round(total/count,2)
print '%.2f'%average
