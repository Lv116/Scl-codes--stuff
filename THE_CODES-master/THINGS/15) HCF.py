def HCF():
    
    A= int(input("Enter First number- "))
    B= int(input("Enter second number- "))
    
    if(A == B):
        print(f"The HCF of the two numbers is {A}...")
    
    while (A != B):        
        if(A > B):
            A = A-B
        else:
            B = B-A
    print (f"The HCF of the two numbers is {A}...")

HCF()
    
