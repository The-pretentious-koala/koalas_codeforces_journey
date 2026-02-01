a,b=map(int,input().split())
flag=0
while(a <= b):
    flag+=1
    a=3*a
    b=2*b
print(flag)