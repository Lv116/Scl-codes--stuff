def  Num_multiple_sum():
    n = input("Enter the number whose sum of first three multiples you want to find-")
    if(n.isdigit()):
        sum = 6*int(n)
        print("The sum of first 3 multiples of",n,"=",sum)
    else:
        print('Enter a number dummy....')
Num_multiple_sum()    
    
