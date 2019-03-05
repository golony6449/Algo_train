##Solution
##입력데이터를 글자별로 분리해, 사전형 자료형에 문자:횟수 형태로 저장
##대소문자를 구분하지 않고, 반환을 대문자로 하기 때문에, 입력 데이터를 전부 대문자로 변환

inputdata=input()

inputdata=inputdata.upper()

dic={}

max_array=['key',0]

isSame=0

for i in inputdata:
    try:
        dic[i]=dic[i]+1
    except:
        dic[i]=1
print(dic)
for k in dic.keys():
    if max_array[1]<dic[k]:
        max_array[0]=k
        max_array[1]=dic[k]
print(max_array)
for k in dic.keys():
    if dic[k]==max_array[1]:
        isSame+=1
    if isSame==2:
        print('?')
        exit()

print(max_array[0])

