print('''░░▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒░░
░░▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒░░ 
░░▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒░░
░░▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▒▒▓▓▒▒░░██░░▒▒▓▓▒▒▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▒▒▒▒  ██░░▒▒▒▒▓▓▓▓▓▓▓▓▓ 
▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓ 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
''')
print("Welcome to Project Treasure Island!\nYour mission is to find the treasure.")
print("*" * 40)
xp = 0

river_choice = input("You're at a river. You can to wait for a boat or swim to the island. What will you do?\n\t"
                     "'swim' or 'wait'\t").lower()
if river_choice == "swim":
    print("You dive into the water and try to swim to the Island...\nUnfortunately, you get attacked by a trout and "
          "lose the game.")
    print(f"Game Over!\n\tYou lost with {xp} XP")
elif river_choice == "wait":
    xp += 10
    print(
        "Safe choice. The boat arrives, floating on it's own. Do you get on the boat or do you wait for it to come back?")
    boat_choice = input("Type 'get on' or 'wait'\t").lower()
    if boat_choice == "wait":
        print("The boat isn't coming back.")
        print(f"Game Over!\n\tYou lost with {xp} XP")
    elif boat_choice == "get on":
        xp += 10
        print(
            "The boat takes you to the island. You see a house with 3 doors. One red, one yellow and one blue. Which one do you choose?")
        door_choice = input("Type 'red', 'yellow' or 'blue'\t").lower()
        if door_choice == "red":
            print("You open the red door and get burned by fire. You lose.")
            print(f"Game Over!\n\tYou lost with {xp} XP")
        elif door_choice == "yellow":
            xp += 10
            print("You open the yellow door and see an skeleton! Do you turn back for safety or go forward?")
            skeleton_choice = input("Type 'turn back' or 'go forward'\t").lower()
            if skeleton_choice == "turn back":
                print("Treasure isn't found by cowards")
                print(f"Game Over!\n\tYou lost with {xp} XP")
            elif skeleton_choice == "go forward":
                xp += 10
                print(
                    "That's the spirit! You move to the next room and find a seagull pecking at the treasure chest. What do you do?")
                seagull_choice = input("Type 'join' or 'distract'\t").lower()
                if seagull_choice == "join":
                    print("The seagull pecks at you and you run away")
                    print(f"Game Over!\n\tYou lost with {xp} XP")
                elif seagull_choice == "distract":
                    xp += 10
                    print(
                        "You throw your remaining bit of food to the seagull and it flies away, leaving you to open the treasure chest. You win!")
                    print(f"Congratulations! You found the treasure with {xp} XP")
            else:
                print(f"Your inability to decide lost you the game\nYou lost with {xp} XP")
        elif door_choice == "blue":
            print("You open the blue door and get eaten by beasts. You lose.")
            print(f"Game Over!\n\tYou lost with {xp} XP")
    else:
        print(f"Sorry, poor decision making doesn't win games. You Lose with {xp} XP")
else:
    print("Sorry, poor decision making doesn't win games. You Lose")
