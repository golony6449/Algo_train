# Sol: 요구사항 구현

shortOne=64
total=64
cnt=1

value=int(input())

while total!=value:
    if total>value:
        shortOne=shortOne/2 #절반으로 자름
        cnt=cnt+1 #막대 절반 -> 갯수 1 증가
        if total-shortOne>=value:
            total=total-shortOne #절반 중 1개 버림
            cnt=cnt-1 #버렸기 때문에 1감소
print(cnt)
