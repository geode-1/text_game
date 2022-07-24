
# Imports

import time

# List of endings got by player
endings_list = []

# defs________

#time delay
def loading():
    for i in range(3):
        time.sleep(0.7)
        print("...")

# endings system
def ending_get(ending):

    if ending == endings_list:
        print(ending)
        time.sleep(0.7)
        loading()
        print("=====" * 34)

    elif ending not in endings_list:
        endings_list.append(ending)
        print(ending)
        time.sleep(0.7)
        loading()
        print("=====" * 34)

def ending_delete():
    while True:
        choice = input("Are you sure to delete your data? (y/n)")
        if choice == "y":
            loading()
            endings_list.clear()
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
    print("=====" * 34)
    while True:
        choice = input("""
    1. Play game
    2. Total endings
    3. Quit
    4. Reset data
        """)
        if choice == "1":
            adventure_start()
            break

        elif choice == "2":
            print("=====" * 34)
            print("Endings collected:", endings_list)

        elif choice == "3":
            print("Thank you for playing the game")
            break

        elif choice == "4":
            ending_delete()
            break

        else:
            print("Enter a valid option")


# Adventure start
def adventure_start():
    print("====="*34)
    global name
    name = input("What is your name?\n")
    while True:

        print(f"{name} is a seal, they wander in the ocean and encounter a school of fish to their left")
        print("and other seals to their right ")
        choice = input("1.Left \n2.Right\n")

        if choice == "1":
            adventure1()
            break

        elif choice == "2":
            adventure2()
            break

        else:
            print ("insert a choice (1 | 2)")

#-----

def adventure1():
    print("=====" * 34)
    while True:

        print(f"{name} stars to chase one of the fish. They almost catch it when they spot a interesting")
        choice = input(" looking structure.\n1. Fish \n2. Interesting structure \n")
        if choice == "1":
            print("=====" * 34)
            print(f"{name} manage to catch and eat the fish, but oh no!! The fish was filed")
            print("with chunks of plastic. They choke and die.")
            ending_get("Ending: Fish")
            menu()
            break

        elif choice == "2":
            adventure1_path1()
            break

        else:
            print("insert a choice (1 | 2)")

def adventure2():
    print("=====" * 34)
    while True:

        print(f"{name} goes to follow the other seals up onto their beach. At the beach is filled with trash.")
        print(f"{name} can follow one of the seals to play in the sand or stay on a rock and relax")
        choice = input("1.Follow seals \n2.Relax \n")

        if choice == "1":
            print("=====" * 34)
            print(f"They follow the other seals, {name} slowly hops on the sand until suddenly they ")
            print(f"feels a sarp pain on them. Sharp pieces of glass from bottles have stabbed the {name}'s stomach")
            print("causing them to eventually bleed to death")
            ending_get("Ending: Glass")
            menu()
            break
        elif choice == "2":
            print("=====" * 34)
            print(f"{name} goes to the top of an rock, but slips back into the ocean on the top of a large pile ")
            print("of plastic. They get entangled in the plastic and suffocates.")
            ending_get("Ending: Plastic")
            menu()
            break
        else:
            print("insert a choice (1 | 2)")

#-----

def adventure1_path1():
    print("=====" * 34)
    while True:

        print(f"{name} goes up to the structure, it looks like a oil rig. They are very curious")
        print("and wishes to explore. There is a large black stain on the surface of the ocean around the big")
        print("concreate structure")
        choice = input("1.Explore black stain\n2.Explore concreate structure\n")

        if choice == "1":
            print("=====" * 34)
            print(f"{name} goes towards the black liquid and it gets stuck on them. They try to swim but")
            print("the oil weights them down, drowning")
            ending_get("Ending: Oiled")
            menu()
            break
        elif choice == "2":
            print("=====" * 34)
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