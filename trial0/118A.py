inp=input().lower()
vowels=['a','e','i','o','u','y']
inp1=[x for x in inp if x not in vowels]
inp2=[x.replace(x,'.'+x) for x in inp1]
print("".join(x for x in inp2))