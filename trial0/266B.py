n,t=map(int,input().split())
inp=list(input())
for _ in range(t):
    i, j = 0, 1
    while j<=n-1:
        if inp[i]=='B' and inp[j]=='G':
            inp[i]='G'
            inp[j]='B'
            i+=2
            j+=2
        else:
            i+=1
            j+=1
print("".join(x for x in inp))