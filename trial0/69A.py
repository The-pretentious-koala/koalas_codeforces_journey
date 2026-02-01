n=int(input())
x_coor=[]
y_coor=[]
z_coor=[]
for i in range(n):
    x,y,z=map(int,input().split())
    x_coor.append(x)
    y_coor.append(y)
    z_coor.append(z)
if sum(x_coor)==0 and sum(y_coor)==0 and sum(z_coor)==0:
    print('YES')
else:
    print('NO')

