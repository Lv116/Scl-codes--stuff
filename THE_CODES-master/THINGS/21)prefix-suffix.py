def prefix_suffix():
    string1= input('ENTER THE FIRST STRING-')
    string2= input('ENTER THE SECOND STRING-')

    S1=list(string1)
    S2=list(string2)
    check=[]
    x=0
    y=0
    z=-1
    m=-1
    while(x<len(S1) and z>-len(S1)):
        if(str(S1[x])==str(S1[y])):
            i=S1[x]
            check.append(i)
            x=x+1
            y=y+1
            l='prefix'
        elif(str(S1[z])==str(S1[m])):
            j=S2[z]
            check.append(j)
            z=z-1
            m=m-1
            l='suffix'
        else:
            break
  
    pr= ["".join(check)] 
    if(l=='prefix'):
        print(f'It is a prefix.\nprefix-{pr[0]}\nMain word-{string2}')
    elif(l=='suffix'):
        print(f'It is a suffix.\nsuffix-{pr[0]}\nMain word-{string2}')
    else:
        print('It is niether a prefix and nor a suffix')
prefix_suffix()
