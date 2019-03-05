def find_start(para):
    point=0
    if para==1:
        return 1,1
    elif para==2:
        return 2,1
    for a in range(1,para):
        point=point+a
        if point>=para:
            return a,para-(point-a)

value=int(raw_input())
start_point,extra=find_start(value)
if start_point%2==0:
      print str(extra)+'/'+str(start_point+1-extra)
else:
  print str(start_point+1-extra)+'/'+str(extra)
