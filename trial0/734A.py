n=int(input())
inp=input()
anton=[x for x in inp if x=='A']
danik=[x for x in inp if x=='D']
print('Anton' if len(anton)>len(danik) else 'Danik' if len(anton)<len(danik) else 'Friendship')