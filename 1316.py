##solution
##2번의 확인을 통해 그룹단어 여부 확인
##1. 체크리스트에 있는가 -> 없으면 추가 (새로운 알파벳 등장 상황)
##2. 체크리스트에 있다 -> 이전글자와 동일 한가 -> 동일하면 계속 진행
##                ->동일 하지 않다 -> 그룹단어 아님 -> False 반
##

#list에서 x 탐색
def find(targetList,x):
    for i in targetList:
        if i==x:
            return True
    return False

# 그룹단어 여부 확인
def check(x):
    checkList=[]
    idx=-1

    for i in x:
        if find(checkList,i)==False:
            checkList.append(i)
##            print('appended! '+i)
        else:
            if i==x[idx]:
                idx=idx+1 # continue 때문에 idx가 증가되지 않아서 별도로 추가
                continue
            else:
##                print('false '+x[idx], idx)
                return False
        
        idx=idx+1

    return True

###test code
##while True:
##    print(check(input()))

## main
recurssion=int(input())

dataList=[]

output=0

#입력
for i in range(recurssion):
    dataList.append(input())

#확인
for x in dataList:
    if check(x)==True:
        output=output+1
print(output)
