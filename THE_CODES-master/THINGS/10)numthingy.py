def odd_even_digits():
    n1 = int(input("Enter the no."))
    n2 = n1
    s_odd=0
    m_even=1

    while (n1>0):
        s_odd= s_odd + n1%10
        n1 = n1//100
    while (n2>1):
        n2 = n2//10
        m_even = m_even * (n2%10)
        n2 = n2//10
    print ("The sum of odd digits is=",s_odd)  
    print ("Product of even digit is=",m_even)
odd_even_digits()
