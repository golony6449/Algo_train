time=int(raw_input())
array=[]
for a in range(time):
      array.append(int(raw_input()))
while True:
      error=0
      for c in range(time-1):
            if array[c]>array[c+1]:
                  temp=array[c]
                  array[c]=array[c+1]
                  array[c+1]=temp
                  error=error+1
      if error==0:
            break
for b in array:
      print b
