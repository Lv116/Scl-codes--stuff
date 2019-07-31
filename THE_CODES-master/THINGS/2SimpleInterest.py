def SI():
    
    p = input("Enter the principle amount- ")
    r = input("Enter the rate of interest-")
    t = input("Enter Time Span (in years) for which you deposited the amount- ")
    if (p.isalpha() or r.isalpha() or t.isalpha()):
        print('ERROR! :(')
    else:
        print(f'The Interest is {eval(p) * eval(r) * eval(t) /100}')

SI()
