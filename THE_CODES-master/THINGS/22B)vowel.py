def vowel():
    inp=input('Enter string-\n')
    x=inp.split(' ')
    v='AaEeIiOoUu'
    y=0
    cnt=0
    lm=[]
    while(y<len(x)):
        if(x[y][0] in v):
            lm.append(x[y])
            cnt+=1
        y+=1
    print(f'{lm} are the words starting with vowels.There are {cnt} such words')
vowel() 
    
    

