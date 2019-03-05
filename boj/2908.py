# solution
# 입력된 숫자(문자열형)을 뒤집어 정수형으로 반환
def reverse(x):
    temp=0
    para=1
    minus=1
    
    for i in x:
        if i=='-':
            minus=-1
            continue
        temp=temp+(para*int(i))
        para=para*10

    return temp*minus
    

rawData=input().split()

reversedValue=[]
for i in rawData:
    reversedValue.append(reverse(i))

print(max(reversedValue[0],reversedValue[1]))


##if reversedValue[0]<reversedValue[1]:
##    print(rawData[1])
##else:
##    print(rawData[0])
