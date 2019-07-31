def Intro_thingy():

    n =input("Enter Name- ")
    a = int(input("Enter Age- "))
    c = int(input("Enter Class- "))

    print(f'    Welcome, {n.capitalize()} \n\
    I am {a} and studying in class {c}\n\
    Last year I was {a-1} years old.')
    if(c>12):
        print('Seriously? Since, when was there a class {c}?')

Intro_thingy()  
    
