def palindrome_check():
    a = int(input("Enter the no. you want to check-\n"))
    b = a
    c = 0
    while(b>0):
        c = c * 10 + b%10
        b = b//10
    if(c == a):
        print(f"The entered no. ({a}) is a Palindrome.",end="\n\n")
    else:
        print(f"The entered no.({a}) isn't a Palindrome.",end="\n\n")
    retry()

def retry():
    i = input("Enter 'YES' if you want to check again and 'NO' if you don't want to... " )
    if (i=='YES'):
        palindrome_check()
    elif(i == 'NO'):
        print('Bye then.....')
    else:
        retry()
            
palindrome_check()        
