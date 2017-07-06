value=int(raw_input())
count=1
ranges=1
while True:
    if value<=ranges:
        print count
        break
    ranges=ranges+(count*6)
    count=count+1
