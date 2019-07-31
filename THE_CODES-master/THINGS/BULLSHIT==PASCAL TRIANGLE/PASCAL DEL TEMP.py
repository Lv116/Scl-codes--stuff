n = int(input('Enter no. of lines'))
pascal = []

for x in range(n):
    if x == 0:
        lis = [1]        
        pascal.append(lis)
        continue
    if x==1:
        lis = [1,1]       
        pascal.append(lis)
        continue

    lis = [l for l in range(x+1)]
    for y in range(1,x):
        lis[0] = 1
        lis[x] = 1 
        lis[y] = pascal[x-1][y] + pascal[x-1][y-1]        

    pascal.append(lis)

print(pascal)

