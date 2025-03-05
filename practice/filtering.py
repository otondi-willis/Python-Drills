n=int(input())
m=n-1
c=[]
while m>=0:
    c.append(m**2)
    m=m-1
for i in reversed(c):
    print(i)