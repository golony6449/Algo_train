def calc(para):
    output=para+(para/1000)+(para/100)%10+(para/10)%10+(para%10)
    return output
para=1
sheet=[]
while True:
    temp=calc(para)
    if temp>calc(10000):
        break
    sheet.append(temp)
    para=para+1
for trigger in range(1,10000+1):
    try:
        sheet.index(trigger)
    except:
        print trigger
