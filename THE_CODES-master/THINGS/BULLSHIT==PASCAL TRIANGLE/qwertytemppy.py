n=int(input('Enter no. of rows'))
trow = [1]
y = [0]
for x in range(max(n,0)):
    print(trow)
    trow=[l+r for l,r in zip(trow+y, y+trow)]

