def calculator():
    c = input('Enter First  number: ')
    d = input('Enter Second number: ')
    if(c.isdigit() and d.isdigit()):
        op = input('''
Enter the operator you want to use:
                          (+ for addition
                          - for subtraction
                          * for multiplication
                          / for division) 
                          ''')
    
        a=int(c)
        b=int(d)
        if (op == '+'):
            print( "=>" ,a , "+" , b)
            print(a + b)
        elif (op == '-'):
            print( "=>" ,a , "-" , b)
            print( a - b)
        elif (op == '*'):
            print( "=>" ,a , "*" , b)
            print(a * b)
        elif (op == '/'):
            print( "=>" ,a , "/" , b)
            if(b!=0):
                print( a / b)
            else:
                print('0 ,Math_Error: Zero Division')
        else:
            print('Invalid operator...')
        retry()
    else:
        print('ERROR, plz enter a NUMBER')
        retry()

def retry():
    A= input('''
Do you want to use the calculator again?
Please type 1 for YES or 0 for NO.
''')

    if (A == '1'):
        calculator()
    elif(A == '0'):
        print('Bye...')
    else:
        retry()
calculator()
