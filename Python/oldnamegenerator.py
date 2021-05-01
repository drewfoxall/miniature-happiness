import random, sys


print("Welcome to the Psych 'Sidekick Name Picker.'\n")
print("A name just like Sean would pick for Gus:\n\n")

first_name = ('Albert','Fred','John','Arthur','Walter','Harry','Thomas','Edward','Henry','Robert')

last_name = ('Smith', 'Jones', 'Taylor', 'Brown', 'Johnson', 'White', 'Green', 'Lewis', 'Clarke', 'Baker')

while True:
    firstName = random.choice(first_name)

    lastName = random.choice(last_name)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Enter no to quit)\n ") 
    if try_again.lower() == "no":
        break
    
    input("\nPress Enter to exit.")