import math
def Series_B():
    print('You can compute the sum of the series- 1/sqrt(2)+2/sqrt(3)+....+n/sqrt(n+1)')
    n = int(input("Enter desired value of n..:-"))
    m=1
    s=0
    while(m<=n):
        s += m/math.sqrt(m+1)
        m += 1
    print(f'sum of series is {s}')
Series_B()
    

