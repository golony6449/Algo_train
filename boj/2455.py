#Sol 타고 내리는 사람을 계산해 승객수를 구하고, 승객수가 maximum보다 크면 maximum 갱신

ride=[]
get_off=[]
for k in range(4):
    temp=input().split()
    get_off.append(int(temp[0]))
    ride.append(int(temp[1]))

people=0
maximum=0

for i in range(4):
    people=people-get_off[i]+ride[i]
    if people>maximum:
        maximum=people

print(maximum)
