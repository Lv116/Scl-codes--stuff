def gamez():
    import random
    for x in range(1):
        x = random.randint(1,20)
        chance=0
        g=0
        print("\nWelcome to the number guessing Game(Only 3 changes allowed)")
        name=input("Hi, What is your Name?- ")
        print(f"Well {name.capitalize()}, I have chosen a number between 1 and 20\nYou have three chances to try and guess it.")
        if (g==x):
            chance += 1
            print("Good job. {name.capitalize()} ,Your answer is correct and you guessed my no. in {chance} chances :)")
        
        while(g!=x and chance<3):
            print("Take a guess")
            g=int(input(""))
            if(g>x):
                print("Your guess is too high...")
                chance+=1
            elif(g<x):
                print("Your guess is too low...")
                chance+=1
            else:
                chance+=1
                print("Good job.",name,"Your answer is correct and you guessed my no. in ", chance,"chances :)")
        if (chance==3 and g!=x):
            print("You were unable to guess my number and lost all 3 chances... :/ The no. was-",x)
        replay()
        
def replay():
    print ("\n\nIf you want to play again type '1' and if you want to leave type '0'")
    c=(input(""))
    if(c=='1'):
        print("LOADING.....")
        print("Restarting game....")
        gamez()
    elif(c=='0'):
        print("Bye, then.....")
    else:
        print("ERROR")
        replay()
gamez()   
