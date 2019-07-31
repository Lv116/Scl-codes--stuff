def pascal_triangle():
    n = int(input('Enter no. of lines- '))
    ls=[]
    for row in range(1,n+1):
        r1=1
        lm=[]
        for i in range(1,row+1):
           lm.append(r1)
           r1=(r1*(row-i))//i 
        ls.append(lm)
    pyramid(n,ls)


def pyramid(x,y):
    for i in range(x):
        print("   "*(x-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(y[i][j]),end=" ",sep=" ")
        print()
pascal_triangle()
