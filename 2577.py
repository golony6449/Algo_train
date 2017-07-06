value=1
output=[]
for a in range(3):
    value=value*int(raw_input())
for b in range(10):
    output.append(0)
string=str(value)
for c in string:
    k=int(c)
    output[k]=output[k]+1
for d in output:
    print d
