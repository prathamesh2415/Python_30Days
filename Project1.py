import random
class Project1:
    def __init__(self,inputnumber) -> None:
       self.inputnumber = inputnumber
        
Target = random.randint(1,100)
print(Target)

while True:
    UserChoice = int(input("Guess the Target Number or Quit(Type Quit):"))
    if(UserChoice == Quit):
        break

    if(UserChoice == Target):
        print("Success: Correct Guess!!")
        break
    elif(UserChoice < Target):
        print("You number was too small. Take a bigger guess........")
    else:
        print("You number was too Big. Take a smaller guess........")
 
 
print("---------------------------GAME OVER --------------------------- ")        