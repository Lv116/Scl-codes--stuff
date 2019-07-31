def Circle_calc():
    r = input('Enter the radius of the circle-')
    if r.isdigit(): 
        a = 3.14*r*r
        c = 2*a/r
        print(f'The area of the circle is- {a} AND The circumference of the circle is- {c}')
    else:
        print('ERROR')
Circle_calc()   
    
