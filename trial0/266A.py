x=int(input())
inp=input()
i=0;j=1
flag=0
while j<=len(inp)-1:
    if inp[i]==inp[j]:
        flag+=1
        i+=1;j+=1
    else:
        i+=1;j+=1
print(flag)

