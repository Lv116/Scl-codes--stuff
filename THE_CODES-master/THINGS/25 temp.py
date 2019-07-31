def histogram():
    print("Type ages the numbers one by one...\n Press Enter when you're done.")
    lst=[]
    freq={}
    while True:
        a=input()
        if(a.isnumeric()):
            n=int(a)
            lst.append(n)
        else:
            break
    ls=lst
    for i in ls:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for j in freq:
        d=0
        kml=[]
        while(d <= j):
            kml.append('*')
            d+=1
        print(j,'-   ',*kml)
        
    
histogram()