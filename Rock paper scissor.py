#CODE

import random
myGuess=str(input("enter your guess : "))

a=['rock','paper','scissor']
cp=random.choice(a)

print("you picked {0}, computer picked {1}".format(myGuess,cp))

if (myGuess==cp):             
    print("Draw match, pick again!")
elif (myGuess=='rock' and cp=='paper'):          
    print("computer won")
elif (myGuess=='rock' and cp=='scissor'):        
    print("You won")
elif (myGuess=='paper' and cp=='rock'):          
    print("You won")
elif (myGuess=='paper' and cp=='scissor'):       
    print("Computer won")
elif (myGuess=='scissor' and cp=='rock'):        
    print("Computer won")
elif (myGuess=='scissor' and cp=='paper'):      
    print("You won")
else:
    print("not picked yet")
