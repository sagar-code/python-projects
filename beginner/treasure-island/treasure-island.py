# 1. Create a greeting for your program.
print("""
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                                                                                 
"""
      )

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

# 2. Ask the user to go left or right.
left_or_right = input('You\'re at a crossroad, where do you want to go? Type "left" or "right" \n').lower()

# 3. Conditions.
if left_or_right == "left":
    # 4. Choose for swim or wait.
    swim_or_wait = input('You\'ve come to lake. There is island in the middle of the lake. Type "wait" to wait for a '
                         'boat. Type "swim" to swim across. \n').lower()
    # 5. Conditions.
    if swim_or_wait == "wait":
       # 6. Choose doors.
        choose_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow,"
                            "and one blue. Which coloure do you choose?")
        # 7. Conditions.
        if choose_door == "red":
           print("It's a room full of fire. Game Over.")
        elif choose_door == "yellow":
           print("You found the treasure! You win!")
        elif choose_door == "blue":
           print("You enter a  room of beasts. Game Over.")
        else:
           print("YOu choose a door that doesn't exist. Game Over.")

    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")