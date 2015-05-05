import random
number_1 = random.randint(1,10)
number_2 = random.randint(1,10)
number_3 = random.randint(1,10)

print("What is " + str(number_1) + " + " + str(number_2) + " + " + str(number_3) + "?")

answer = number_1 + number_2 + number_3
user_input = int(input())

if (user_input == answer):
    # User response correct
    print("That's correct")
else:
    # User response wron
    print("Sorry, your did it wrong.")
    print("The answer is: ", str(answer))
    
    