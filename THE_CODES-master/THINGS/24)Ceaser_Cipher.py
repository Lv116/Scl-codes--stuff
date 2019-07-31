#vyomjainpr24:tm:
def program():
    print('Hello, User. This is the encryption-decryption program.\n\
Press ENTER to continue.')
    enter=input('')
    history=[]
    if (enter.isdigit()):
        print('Program Terminated')
    else:
        print('||||Launching Program...')
        menu(history)
def menu(history):
    print('Welcome to the Cipher Code menu...')
    print("           Press '1' to access the encryption interface.\n\
           Press '2' to access the decryption interface.\n\
           Press '3' to access your last few encryptions and decryptions.\n\
           Press '4' to exit the menu")
    key=input('ENTER YOUR CHOICE:')
    if (key=='1'):
        encrypt(history)
    elif(key=='2'):
        decrypt(history)
    elif(key=='3'):
        print('Initiating....\n\n\n')
        print(*history, sep='\n\n')
        retry(history)
    elif(key=='4'):
        print('Exiting Menu.Bye...')
        

def encrypt(history):
    check='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    check2='abcdefghijklmnopqrstuvwxyz'
    st= input('Enter the string you want to encrypt-\n')
    rot=input('Enter no. of rotations-')
    if (rot.isdigit()):
        rot=rot
    else:
        rot='13'
    m=st.split()
    i=0
    lm=[]
    for j in range(0,len(m)):
        n=m[j]
        lm.append([])
        for k in range (0,len(n)):
            o=n[k]
    
            if(o.isupper()):
                x=(check.find(o)+int(rot))%26
                y=check[x]
            elif(o.islower()):
                x=(check2.find(o)+int(rot))%26
                y=check2[x]
            lm[i].append(y) 
        i+=1    
    q=0
    wer=[]
    while(q<len(m)):
        p=lm[q]
        s=[str(w) for w in p]
        res=["".join(s)]
        rt=res[0]
        wer.append(rt)
        q+=1
    gah=' '
    gah=gah.join(wer)
    print(gah)
    history.append('*'+st + ' rot-'+ rot + ':encryption' + '=' + gah )
    retry(history)

def decrypt(history):
    inp=input('Enter encryption-\n')
    rot=input('Enter no.of rotations of the encryption-')
    check='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    check2='abcdefghijklmnopqrstuvwxyz'
    m=inp.split()
    if(rot.isdigit()):
        rot = rot
    else:
        rot='13'
    i=0
    lm=[]
    for j in range(0,len(m)):
        n=m[j]
        lm.append([])
        for k in range (0,len(n)):
            o=n[k]
    
            if(o.isupper()):
                x=(check.find(o)-int(rot))%26
                y=check[x]
            elif(o.islower()):
                x=(check2.find(o)-int(rot))%26
                y=check2[x]
            lm[i].append(y) 
        i+=1    
    q=0
    wer=[]
    while(q<len(m)):
        p=lm[q]
        s=[str(w) for w in p]
        res=["".join(s)]
        rt=res[0]
        wer.append(rt)
        q+=1
    gah=' '
    gah=gah.join(wer)
    print(gah)
    history.append('*' +inp + ' rot-'+ rot + ':decryption' + '=' + gah )
    retry(history)
def retry(history):
    A= input('''
Do you want to use the Cipher Code menu again?
Please type 1 for YES or 0 for NO.
''')
    if (A == '1'):
        menu(history)
    elif(A == '0'):
        print('Program Terminated...')
program()