x=int(input())
for i in range(x):
    inp=input()
    print(inp[0]+str(len(inp)-2)+inp[-1] if len(inp)>10 else inp)