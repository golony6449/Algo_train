total=int(raw_input())
kg5=total/5
others=total%5
kg3=others/3
if others%3==0:
    print kg5+kg3
    exit()
else:
    while True:
        if kg5==0:
            break
        kg5=kg5-1
        others=others+5
        if others%3==0:
            print kg5+(others/3)
            exit()
print -1
