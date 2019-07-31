def NUM():      
    n = input("Type 'YES' if you want to print numbers between 2000 and 3200 that are divisible by 7 but aren't multiples of 5-")
    if (n =='YES'):
        num()
def num():
    a=2002
    num=[a]
    while(a>=2000 and a<=3200):
        a+=7
        if (a%5!=0):
             num.append(a)
    print(num)
     
NUM()   
    




