# Solution: 전체가 몇일 인지 구한 뒤, 날짜 수를 이용해 계산

inputdata=input().split()

x=int(inputdata[0])
y=int(inputdata[1])

totalday=[31,28,31,30,31,30,31,31,30,31,30,31]

total=y

#Total date calculate
if x!=1:
    for i in range(x-1):
        total=total+totalday[i]

rest=total%7
if rest==1:
    print('MON')
elif rest==2:
    print('TUE')
elif rest==3:
    print('WED')
elif rest==4:
    print('THU')
elif rest==5:
    print('FRI')
elif rest==6:
    print('SAT')
else:
    print('SUN')
