def Series_A():
    print('You can evaluate the sum of the series - x+x^2/2+x^3/3..........+x^n/n')
    x = eval(input("Enter desired value of x...:"))
    t= int(input("Enter the no. of terms in the series...:"))
    n=1
    s=0
    while(n<=t):
        s += (x**n)/n
        n += 1
    print(s)
Series_A()
    

