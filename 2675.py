time=int(input())
for a in range(time):
    value=raw_input().split()
    repeat=int(value[0])
    string=value[1]
    length=len(string)
    output=''
    for b in range(length):
        output=output+string[b]*repeat
    print output
    
