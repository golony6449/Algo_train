time=int(raw_input())
for a in range(time):
    input_v=raw_input().split()
    count=int(input_v[0])
    total=0.0
    for b in range(count):
        total=total+float(input_v[b+1])
    average=total/count
    over_a=0.0
    for c in range(count):
        if average<float(input_v[c+1]):
            over_a=over_a+1
    print '%.3f%%'%(round(over_a/count*100,3))
