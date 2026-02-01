loop=int(input())
res=0
for i in range(loop):
    inp=input()
    if(inp=='++X' or inp=='X++'):
        res+=1
    else:
        res-=1
print(res)