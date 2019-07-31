def Denomination():
    m= input("Enter the amount you want to denominate-")
    if(m.isdigit()):
        n= int(m)
        print("No. of Rs.1000 notes required=",n//1000,
              "\nNo.of Rs.500 notes required=",(n%1000)//500,
              "\nNo. of Rs.100 notes required=",((n%1000)%500)//100,
              "\nNo. of Rs.50 notes required=",(((n%1000)%500)%100)//50,
              "\nNo. of Rs.10 notes required=",((((n%1000)%500)%100)%50)//10,
              "\nNo. of Rs.5 notes required=",(((((n%1000)%500)%100)%50)%10)//5,
              "\nNo. of Rs.2 notes required=",((((((n%1000)%500)%100)%50)%10)%5)//2,
              "\nNo. of Rs.1 notes required=",(((((((n%1000)%500)%100)%50)%10)%5)%2)//1)
    else:
        print('ERROR...')
    retry()

def retry():
    A= input('''
Do you want to use the denominator again?
Please type 1 for YES or 0 for NO.
''')

    if (A == '1'):
        Denomination()
    elif(A == '0'):
        print('Bye...')
    else:
        print('ERROR!')
        retry()
Denomination() 
    
