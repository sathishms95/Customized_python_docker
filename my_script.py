n=15
for i in range(0,1):
    print(((n-(i+1))*' ')+(((2*i)+1)*'*'))
for i in range(i,n):
    print(((i)*'')+(((((n-i)*2)-1)*'*')))