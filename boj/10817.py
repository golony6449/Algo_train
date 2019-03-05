value=raw_input().split()
output=[]
for a in range(3):
    output.append(int(value[a]))
for b in range(2):
    for c in range(2):
        if output[c]<output[c+1]:
            temp=output[c]
            output[c]=output[c+1]
            output[c+1]=temp
print output[1]
