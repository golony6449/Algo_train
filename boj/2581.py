def checker(para):
      if para==1:
            return False
      for a in range(2,para-1):
            if para%a==0:
                  return False
      return True

m=int(raw_input())
n=int(raw_input())
total=0
minimum=0
for b in range(m,n+1):
      if minimum==0 and checker(b)==True:
            minimum=b
            total=total+b
      elif checker(b)==True:
            total=total+b
if total==0:
      print -1
else:
      print total
      print minimum
