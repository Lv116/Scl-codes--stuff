def ISBN():
    n = input("Enter 10 digit ISBN code- ")
    if(len(n) != 10):
        print("ERROR....." ,
              "|||ISBN must be 10 digit :/")
        ISBN()
    else:
        s=(1*int(n[0])\
           +2*int(n[1])\
           +3*int(n[2])\
           +4*int(n[3])\
           +5*int(n[4])\
           +6*int(n[5])\
           +7*int(n[6])\
           +8*int(n[7])\
           +9*int(n[8]))%11
        if(s == int(n[-1])):
            print("||||The entered ISBN is correct... :)")
        else:
            print("||||Incorrect ISBN. Try Again.... :/")
        ISBN()             
ISBN()



