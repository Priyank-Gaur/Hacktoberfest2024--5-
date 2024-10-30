a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    b=1
    for j in range(1,i+1):
        b=j*b
    c+=b
print(c)
