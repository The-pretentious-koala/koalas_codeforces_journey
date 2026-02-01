inp=input()
inp=str(int(inp)+1)
while(True):
    if len(set(inp))==4:
        break
    else:
        inp=str(int(inp)+1)
print(inp)


