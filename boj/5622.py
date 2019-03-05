

rawData=input()
dic={'c=':0,'c-':0,'dz=':0,'d-':0,'lj':0,'nj':0,'s=':0,'z=':0}
temp=''
count=0

for i in rawData:
    temp=temp+i
    if len(temp)==2:
        for j in dic.keys():
            if temp==j:
                count

#작성
