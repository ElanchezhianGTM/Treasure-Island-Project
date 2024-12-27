import variable

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road where do you want to go?")
first_choice = input("Type 'left' or 'right'\n")
variable.lower(first_choice)
if first_choice == "left":
    print("You have come to a lake. There is island in the middle of the lake.")
    second_choice = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    variable.lower(second_choice)
    if second_choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        third_choice = input("One red, one yellow and one blue. which colour do you choose?\n")
        variable.lower(third_choice)
        if third_choice == "red":
            print("It's a room full of fire. Game over.")
        elif third_choice == "blue":
            print("It's a room full of beasts. Game over.")
        else:
            print("You found the treasure! You win!")
    else:
        print("You get attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game Over.")