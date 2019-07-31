def farm_thingy():

    h = int(input('Enter number of heads:'))
    l = int(input('Enter number of legs:'))
    r = abs(l-2*h)//2 #no. of rabbits
    c = (h-r) #no. of chickens

    print(f'No. of rabits: {r}')
    print(f'No. of chickens: {c}')

farm_thingy()









