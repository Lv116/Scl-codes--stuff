def ticket():

    def Speed1():
        if(v>=86):
            print ("You got a big ticket","2= big ticket")
        elif(66<=v<=85):
            print('You got a small ticket. 0=small ticket')
        else:
            print('0=no ticket. You got no ticket')
                #defines function for speed for birthday
     
    def Speed2():
        if(v>=81):
            print ("You got a big ticket","2= big ticket")
        elif(61<=v<=80):
            print('You got a small ticket. 0=small ticket')
        else:
            print('0=no ticket. You got no ticket')
                 #defines function for speed for NORMAL DAY
    

    v=int(input('Enter speed'))
    A=int(input('If you have your birthday type 1 and if not type 0.')) 

    if (A == 1):
        Speed1()
                
    if (A == 0):
        Speed2()
            
ticket()

        
        
        
        
        
        
        
