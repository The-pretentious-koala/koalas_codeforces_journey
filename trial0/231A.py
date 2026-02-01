loop=int(input())
res=0
for i in range(loop):
    x,y,z=map(int,input().split())
    if x+y+z>=2:
        res+=1
    else:
        continue
print(res)
