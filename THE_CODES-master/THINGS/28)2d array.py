def _2DArray():
    print('Genherate a 2 dimensional array....')
    x=int(input('Enter the value of X- '))
    y=int(input('Enter the value of Y- '))
    ls=[]
    for i in range(0,x):
        lm=[]
        for j in range(0,y):
            k=j*i
            lm.append(k)
        ls.append(lm)
    print(ls)
 
_2DArray()