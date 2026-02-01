a=input().lower()
b=input().lower()
flag=False
res=0
for i in range(max(len(a),len(b))):
    res=ord(a[i])-ord(b[i])
    if res>0:
        print(1)
        flag=True
        break
    elif res==0:
        continue
    else:
        print(-1)
        flag=True
        break
if flag==False:
    print(0)