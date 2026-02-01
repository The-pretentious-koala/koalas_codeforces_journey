inp=input()
inp_lower=[x for x in inp if x.islower()]
inp_upper=[x for x in inp if x.isupper()]
res=inp.lower() if len(inp_lower)>len(inp_upper) else inp.upper() if len(inp_lower)<len(inp_upper) else inp.lower()
print(res)