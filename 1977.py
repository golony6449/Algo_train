first=int(raw_input())
second=int(raw_input())
total=0
minimum=0
for a in range(10000000):
    if a**2>second:
        break
    elif a**2>=first:
        total=total+a**2
        if minimum==0:
            minimum=a**2
if minimum==0:
    print -1
    exit()
print total
print minimum
