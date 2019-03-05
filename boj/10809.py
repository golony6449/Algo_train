value=raw_input()
output=[]
count=0
for a in range(122-97+1):
    output.append(-1)
for b in value:
    k=ord(b)
    if output[k-97]==-1:
        output[k-97]=count
    count=count+1
for c in output:
    print c,
