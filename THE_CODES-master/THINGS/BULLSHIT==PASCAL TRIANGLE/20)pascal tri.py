n=int(input("Enter number of rows in the Pascaline Triangle-"))
p=[]
for i in range(n):
    p.append([])
    p[i].append(1)
    for j in range(1,i):
        p[i].append(p[i-1][j-1]+p[i-1][j])
    if(n!=0):
        p[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(p[i][j]),end=" ",sep=" ")
    print()
