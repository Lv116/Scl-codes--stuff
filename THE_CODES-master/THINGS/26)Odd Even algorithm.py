def algo_num_list():
    a= eval(input("Enter the number"))
    
    val_1=[a]
    val_2=[a]
    
    if (a%10==0):
        val_2.remove(a)
    if(a==0):
        print("Error....-No.can't be 0")
    if(a==1):
         print(a)
         
    while(a!=1):
        if (a%2==0):
             a=a//2
        else:
             a=(a*3)+1
        val_1.append(a)
        val_2.append(a)
        if (a%10==0):
            val_2.remove(a)
    print(val_1)   
    print("A) No. of elements in the list are-", len(val_1))
    print("B) If we remove all the occurances of multiples of 10 then the list becomes", val_2)
algo_num_list() 


 
       
    
    
    
        
    
      
    
       
      
          
             
    
