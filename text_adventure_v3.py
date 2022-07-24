
# Imports

import time

# List of endings got by player
endings_list = []
global score
score = 0

# defs________

#time delay
def loading():
    for i in range(3):
        time.sleep(0.7)
        print("...")

# endings system
def ending_get(ending):

    if ending in endings_list:
        global score
        print(ending)
        time.sleep(0.5)
        score += 3
        loading()
        time.sleep(0.5)
        seperator()

    elif ending not in endings_list:
        endings_list.append(ending)
        print(ending)
        score += 5
        loading()
        time.sleep(0.5)
        seperator()

#reward system
def seperator():
    if score >= 25:
        print("*=*=*=" * 29)
    else:
        print("======" * 29)

def data_delete():
    while True:
        choice = input("Are you sure to delete your data? (y/n)\n")
        if choice == "y":
            loading()
            endings_list.clear()
            global score
            score = 0
            time.sleep(0.7)
            print("Done! Data deleted")
            print(endings_list)
            menu()
            break
        elif choice == "n":
            print("Ok, we will go back to the menu instead")
            menu()
            break
        else:
            print("Please respond with (y/ n)")

# Menu
def menu():
    seperator()
    while True:
        choice = input("""
    1. Play game
    2. Stats
    3. Quit
    4. Reset data
        """)
        if choice == "1":
            adventure_start()
            break

        elif choice == "2":
            seperator()
            print("Endings collected:", endings_list)
            print("Score", score)

        elif choice == "3":
            print("Thank you for playing the game")
            break

        elif choice == "4":
            data_delete()
            break

        else:
            print("Enter a valid option")


# Adventure start
def adventure_start():
    seperator()
    global name
    name = input("What is your name?\n")
    while True:

        print(f"{name} is a seal, they wander in the ocean and encounter a school of fish to their left")
        print("and other seals to their right ")
        choice = input("1.Left \n2.Right\n").lower()

        if choice == "1" or "left":
            adventure1()
            break

        elif choice == "2" or "right":
            adventure2()
            break

        else:
            print("insert a choice (1 | 2)")

#-----

def adventure1():
    seperator()
    while True:

        print(f"{name} stars to chase one of the fish. They almost catch it when they spot a interesting")
        choice = input(" looking structure.\n1. Fish \n2. Interesting structure \n").lower()
        if choice == "1":
            seperator()
            print(f"{name} manage to catch and eat the fish, but oh no!! The fish was filed")
            print("with chunks of plastic. They choke and die.")
            ending_get("Ending: Fish")
            menu()
            break

        elif choice == "2" or "interesting structure":
            adventure1_path1()
            break

        else:
            print("insert a choice (1 | 2)")

def adventure2():
    seperator()
    while True:

        print(f"{name} goes to follow the other seals up onto their beach. At the beach is filled with trash.")
        print(f"{name} can follow one of the seals to play in the sand or stay on a rock and relax")
        choice = input("1.Follow seals \n2.Relax \n").lower()

        if choice == "1" or "follow seals":
            seperator()
            print(f"They follow the other seals, {name} slowly hops on the sand until suddenly they ")
            print(f"feels a sarp pain on them. Sharp pieces of glass from bottles have stabbed the {name}'s stomach")
            print("causing them to eventually bleed to death")
            ending_get("Ending: Glass")
            menu()
            break
        elif choice == "2" or "relax":
            seperator()
            print(f"{name} goes to the top of an rock, but slips back into the ocean on the top of a large pile ")
            print("of plastic. They get entangled in the plastic and suffocates.")
            ending_get("Ending: Plastic")
            menu()
            break
        else:
            print("insert a choice (1 | 2)")

#-----

def adventure1_path1():
    seperator()
    while True:

        print(f"{name} goes up to the structure, it looks like a oil rig. They are very curious")
        print("and wishes to explore. There is a large black stain on the surface of the ocean around the big")
        print("concreate structure")
        choice = input("1.Explore black stain\n2.Explore concreate structure\n").lower()

        if choice == "1" or "explore black stain":
            seperator()
            print(f"{name} goes towards the black liquid and it gets stuck on them. They try to swim but")
            print("the oil weights them down, drowning")
            ending_get("Ending: Oiled")
            menu()
            break
        elif choice == "2" or "explore concreate structure":
            seperator()
            print(f"{name} gets close to the structure and hears some yelling noises along with a sound")
            print("with a bright light above the water. They poke their head above the water to see ")
            print(f"a large flash followed by a explosion, with a large metal debris hitting {name}")
            ending_get("Ending: Boom")
            menu()
            break
        else:
            print("insert a choice (1 | 2)")

# _______
# code


loading()

menu()
