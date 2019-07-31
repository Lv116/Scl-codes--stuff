
def string():
    print('Please refer to below for the operation you want to do\n\
          1- FREQUENCY OF ALL CHARACTERS\n\
          2- WORD OF HIGHEST LENGTH\n\
          3- THE STRING IN TITLE CASE\n\
          4- READ FULL NAME OF PERSON AND PRINT ONLY THE INITIALS')
    inp=input('Enter the type of conversion you want to execute-')
    
    if(inp=='1'):
       frequency()  
    elif(inp=='2'):
        highest_length()
    elif(inp=='3'):
        Title()
    elif(inp=='4'):
        Name()
    else:
        print('ERROR!!!Plz Retry-')
    retry()




def frequency():
    st = input('Enter the string you want to operate-\n')
    st1=st
    freq={}
    for i in st1:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(f'frequency of each character in "{st1}" is -\n {str(freq)}')
def highest_length():
    st = input('Enter the string you want to operate-\n')
    m=st.split(' ')
    word =  max(m, key=len)
    print(f'The longest word is-"{word}"of length = {len(word)}')
def Title():
    st = input('Enter the string you want to operate-\n')
    m=st.title()
    print(m)
def Name():
    st = input('Enter the string you want to operate-\n')
    m=st.split(' ')
    n=''
    for i in range(len(m)-1):
        l=m[i]
        n+=(l[0].upper()+' ')
    n+=m[-1].title()
    print(f'The initials are\n{n}')
    
def retry():
    A= input('''
Do you want to use the string converter again?
Please type 1 for YES or 0 for NO.
''')

    if (A == '1'):
        string()
    elif(A == '0'):
        print('Bye...')
    else:
        retry()  

string()
