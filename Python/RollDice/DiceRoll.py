import random
negative = ["No","no","NO","Nah","nah","NAH"]
def GetNumber():
    Random_Num = random.randint(1,7)
    print(Random_Num)

GetNumber()

input(print("Do you want to roll again? "))

if input not in negative:
    GetNumber()
    
        