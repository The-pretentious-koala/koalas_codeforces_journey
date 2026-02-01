inp=input()
lucky=['4','7']
count=[x for x in inp if x in lucky]
if len(count)==4 or len(count)==7:
    print('YES')
else:
    print('NO')