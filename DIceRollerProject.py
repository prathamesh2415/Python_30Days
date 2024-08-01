import random

#DiceRoller = random.randint(1,6)
#print("Dice is rolled...............")
#print("Dice shows the number....",DiceRoller)

class DicRoller:
    print("Dice is rolling...............")
    def ShowNumber(self):
       DiceRollNumber = random.randint(1,6)
       print("--------")
       print("|       |")
       print("|  {DiceRollNumber}    |")
       print("|       |")
       print("--------")
      # print("Dice shows the number....",DiceRollNumber)
    
D1 = DicRoller()
D1.ShowNumber()