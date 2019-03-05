def isprime(para):
      if para==1:
            return False
      for a in range(2,para):
            if para%a==0:
                  return False
      return True

time=int(raw_input())
array=raw_input().split()
count=0
for b in range(time):
      temp=int(array[b])
      if isprime(temp):
            count=count+1
print count
