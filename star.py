n=int(input("rows"))
for i in range(0,n+1):
    for j in range(0,1+i):
        print('*',end=" ")
    print( )
for i in range(0,n-1):
    for j in range(0,n-1-i):
        print('*',end=" ")
    print()

