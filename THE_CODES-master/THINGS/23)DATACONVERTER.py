def datacv():
    
    inp = int(input('Enter the No. you want to convert....-'))
    print('Conversion type key-\n B-Binary \n O-Octal \n H-Hexadecimal')
    typ = input("Which type of conversion do you want to execute...-")
    a = inp 
    ls=[]
    k=1
    if (typ=='B'):
        if (a==0):
            ls.append(0)
        if (a==1):
            ls.append(1)
        while(a>=1):
            b=a
            if(a!=3):
                a=a//2
                if (a>=1):
                    l=b%a
                    ls.insert(0,l)
                elif(a>=0):
                    ls.insert(0,k)
            else:
                ls.insert(0,k)
                a=1    
    
    elif(typ=='O'):
        while(a>0):
            b=a%8
            a=(a-b)//8
            ls.insert(0,b)

    elif(typ=='H'):
        while(a>0):
            b=a%16
            a=(a-b)//16
            if (b<=9):
                ls.insert(0,b)
            else:
                lst=['A','B','C','D','E','F']
                c=lst[b-10]
                ls.insert(0,c)
    s = [str(i) for i in ls]          
    res= ["".join(s)]
    print(res[0])
    retry()
def retry():
    A= input('''
Do you want to use the converter again?
Please type 1 for YES or 0 for NO.
''')
    if (A == '1'):
        datacv()
    elif(A == '0'):
        print('Bye...')
    else:
        retry()
datacv()
