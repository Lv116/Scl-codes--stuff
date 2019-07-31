def date():
    d=int(input('Enter Date:'))
    m=int(input('Enter Month:'))
    y=input('Enter Year:')
    L=["JAN","FEB","MAR","APR","MAY", "JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    if(m<=12 and d<=31 and int(y)%100 != 0):
        print(f'The Date is-{d}-{L[m-1]}-{int(y)%100}')
    elif(m<=12 and d<=31):
        print(f'The Date is-{d}-{L[m-1]}-{y[-3]+y[-2]+y[-1]}')
    else:
        print("The date entered can't exist :(")
 
date()














