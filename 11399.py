person=int(raw_input())
time=[]
for i in raw_input().split():
    time.append(int(i))
time.sort()
output=0
for j in range(person+1):
    temp=0
    for k in range(j):
        temp=temp+time[k]
    output=output+temp
print output
