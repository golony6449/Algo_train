time=int(raw_input())
add_point=0
for a in range(time):
    total=0
    value=raw_input()
    length=len(value)
    for b in value:
        if b=='O':
            total=total+1+add_point
            add_point=add_point+1
        else:
            add_point=0
    print total
    add_point=0
