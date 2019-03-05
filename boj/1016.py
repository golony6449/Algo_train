#Sol: 입력범위의 갯수에서 나누어 지는 수의 갯수를 빼서 계산
# 수정

def calc(data):
    limit=100001+data[1]
    cnt=0
    
    for k in range(data[0],data[1]+1):
        for j in range(2, limit):
            if k<(j**2):
                break
            if k%(j**2)==0:
                #print(k,j)
                cnt=cnt+1
                break

    return cnt


value=[]
for k in input().split():
    value.append(int(k))



output=value[1]-value[0] +1
sqr_cnt=calc(value)

print(output-sqr_cnt)
