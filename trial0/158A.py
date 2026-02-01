n, k = map(int, input().split())
pos = list(map(int, input().split()))
res=[x for x in pos if x>=pos[k-1] and x>0]
print(len(res))

