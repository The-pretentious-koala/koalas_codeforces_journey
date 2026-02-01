n=int(input())
currpass=0
currpassls=[currpass]
for i in range(n):
    exit,enter=map(int,input().split())
    currpass=currpass-exit+enter
    currpassls.append(currpass)

print(max(currpassls))
