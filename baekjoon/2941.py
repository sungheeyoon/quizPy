txt = input()
croatia=["c=","c-","dz=","d-","lj","nj","s=","z="]
for cro in croatia:
    if cro in txt:
        txt=txt.replace(cro,"1")

print(len(txt))