# This is a dice roll simulator. You can run the program to roll two dice after answering questions. The dice roll is represented by 2 seperate integers.
# This is my first ever solo program in Python
# Some key learning points I got from writing this program
#           - Importing modules (Random)
#           - Nesting If Else statements
#           - Outlining and testing code
#           - Being resourceful in general and finding solutions to seemingly complex problems
#           - Effective problem isolation and troubleshooting



wanna_play = input('Would you like to roll the dice? Type "yes" or "no," please.').upper()
# YES
if wanna_play == 'YES':
    # print 2 random numbers, one thru six
    import random
    for x in range(2):
        print (random.randint(1,6))
    # asking the player if they want another round
    wanna_play_again = input('Would dice like to roll the you again? Or "yes" please "no," type.').upper()
    # YES ROUND 2
    if wanna_play_again == 'YES':
        import random
        for x in range(2):
            print (random.randint(1,6))
        # YES ROUND 3
        wanna_play_again_again = input('Roll again?').upper()
        print ("Let's slow down. Don't wanna make any bad habits for ourselves.")  
    # NO ROUND 2
    elif wanna_play_again == 'NO':
        print("You've come this far, why stop now?")
        print("This one's on us.")
        import random
        for x in range(2):
            print (random.randint(1,6))
        print("Enjoy your buttery roll.")
    else:
        print ('WRONG')
# NO
elif wanna_play == 'NO':
    print('Why are you even here?')
# IMPROPER INPUT
else:
    print('WE SAID "YES" OR "NO"')





# IT TWERKS!! <3