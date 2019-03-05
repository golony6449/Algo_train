input_v=raw_input().split()
array=['1','2','3','4','5','6','7','8']
if input_v==array:
    print 'ascending'
    exit()
    
array.reverse()
if input_v==array:
    print 'descending'
else:
    print 'mixed'
