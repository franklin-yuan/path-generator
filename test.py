import hermite as hm

ar = []
for i in range(10):
    ar.append(hm.segment())
    
print(ar)

ar[0].concluded = True

for i in range(10):
    print(ar[i].concluded)