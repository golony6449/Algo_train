def calc(value):
   sum=value/10+value%10
   output=(value%10)*10+sum%10
   return output

input_v=int(raw_input())
count=1
result=calc(input_v)
while True:
    if input_v==result:
        print count
        break
    else:
        result=calc(result)
        count=count+1
