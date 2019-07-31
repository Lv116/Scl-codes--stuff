def Bill_Charges():
    u = int(input("Enter units consumed-"))
    if (u <= 100):
        b = (u*0.4)+50
    elif (u <= 300):
        b = 40+((u-100)*0.5)+50   
    else:
        b = 40+(200*0.5)+((u-300)*0.6)+50
    print(f'Electical charges - Rs. {b}')
    
Bill_Charges()
