import sys

input_v=raw_input()
count=0
while True:
    for i in range(10):
        try:
            sys.stdout.write(input_v[i+count])
            if i==9:
                count=count+10
                print
        except:
            exit()
