k,n,w=map(int,input().split())
tot=0
for i in range(1,w+1):
    tot=tot+(i*k)
borrow_amount=tot-n if (tot-n)>0 else 0
print(borrow_amount)
