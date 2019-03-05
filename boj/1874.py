def push(para):
    stack.append(para)
    print ('+')
def pop():
    print ('-')
    output.append(stack.pop())
    
time=int(input())
target=[]
stack=[]
output=[] #empty -> same as target
now_process=0
parameter=0 #

#save input value in target
for a in range(time):
    k=int(input())
    target.append(k)
    
#find first value 
for b in range(1,time+1):
    if b!=target[0]:
        push(b)
    else:
        parameter=b+1
        push(b)
        pop()
        now_process=now_process+1
        break
#main algorithm
while True:
    try:
        if target[now_process]==stack[-1]:
            pop()
            now_process=now_process+1
            print ('case1')
        else:
            push(parameter)
            parameter=parameter+1
            print ('case2')
    except: #When the target is ascending order
        if target[now_process]==parameter:
            push(parameter)
            pop()
            now_process=now_process+1
            parameter=parameter+1
            print ('case3')
        else:
            push(parameter)
            parameter=parameter+1
            print ('case4')
    if time==len(output):
        break

#problem [1,5,2,4,3]
