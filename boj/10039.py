input_a=[]
total=0
for i in range(5):
    temp=int(raw_input())
    if temp < 40:
        temp=40
    input_a.append(temp)
for j in input_a:
    total=total+j
print total/5
