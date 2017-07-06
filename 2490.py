for i in range(3):
    array=raw_input().split()
    count_0=0
    for j in array:
        if int(j)==0:
            count_0=count_0+1
    if count_0==0:
        print 'E'
    elif count_0==1:
        print 'A'
    elif count_0==2:
        print 'B'
    elif count_0==3:
        print 'C'
    elif count_0==4:
        print 'D'
