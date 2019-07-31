def Age():
    print("Type ages of students one by one in NUMERICAL value...\n")
    A=0
    B=0
    C=0
    D=0
    while True:
        a=input()
        if(a.isnumeric()):
            n=int(a)
            if (n<12):
                D = D + 1
            elif(n<15):
                A = A + 1
            elif(n<17):
                B = B + 1
            else:
                C = C + 1
        else:
            break
        
        
    print("GROUP A: 12 yrs. and above but less than 15-",A,
          "\nGROUP B: 15 yrs. and above but less than 17-",B,
          "\nGROUP C: 17 yrs. and above but less than 19-",C,
          "\nGROUP D: Lesser than 12 yrs.-",D)
Age()
