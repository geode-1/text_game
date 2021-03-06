
# Import(s)

import time

# list of list of all endings and facts
ending_fact = [["Ending: Fish", "Ending: Glass", "Ending: Plastic", "Ending: Oiled", "Ending: Boom",],
               [
           "Fact: Microplastics are fragments of any type of plastic less than 5 mm in length",
           "Fact: The Great Pacific Garbage Patch is a collection of marine debris in the North Pacific Ocean.",
           "Fact: Thousands of seabirds and sea turtles, seals and other marine mammals are killed each year",
           "Fact: Oil spreads over the surface of water in a thin layer that stops oxygen getting to the wildlife",
           "Fact: Oil  can disrupt animals' communication, breeding and nesting with loud noises and human movement."
           ]]
# List of endings gotten by player
endings_list = []
global score
score = 0

# _____________defs_____________

# time delay giving an extra effect to the game


def loading():
    for i in range(3):
        time.sleep(0.7)
        print("...")


# Endings system that will fill up 'endings_list' and show facts
def ending_get(ending, fact):

    if ending in endings_list:
        global score
        print(ending)
        print(fact)
        time.sleep(0.5)
        score += 3
        loading()
        time.sleep(0.5)
        seperator()

    elif ending not in endings_list:
        endings_list.append(ending)
        print(ending)
        print(fact)
        score += 5
        loading()
        time.sleep(0.5)
        seperator()

# Method to make it easier to separate and read the writing + reward system
def seperator():
    if score >= 25:
        print("*=*=*=" * 29)
    else:
        print("======" * 29)

# Deletes all data the player has
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

# Menu with 4 options
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


# Adventure start, the game itself with different paths
def adventure_start():
    seperator()
    global name
    name = input("What is your name?\n")
    while True:

        print(f"{name} is a seal, they wander in the ocean and encounter a school of fish to their left")
        print("and other seals to their right ")
        choice = input("1.Left \n2.Right\n").lower()

        if choice == "1":
            adventure1()
            break

        elif choice == "2":
            adventure2()
            break

        else:
            print("insert a choice (1 | 2)")

#----------------

def adventure1():
    seperator()
    while True:

        print(f"{name} stars to chase one of the fish. They almost catch it when they spot a interesting")
        choice = input(" looking structure.\n1. Fish \n2. Interesting structure \n").lower()
        if choice == "1":
            seperator()
            print(f"{name} manage to catch and eat the fish, but oh no!! The fish was filed")
            print("with chunks of plastic. They choke and die.")
            ending_get(ending_fact[0][0], ending_fact[1][0])
            menu()
            break

        elif choice == "2":
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

        if choice == "1":
            seperator()
            print(f"They follow the other seals, {name} slowly hops on the sand until suddenly they ")
            print(f"feels a sarp pain on them. Sharp pieces of glass from bottles have stabbed the {name}'s stomach")
            print("causing them to eventually bleed to death")
            ending_get(ending_fact[0][1], ending_fact[1][1])
            menu()
            break
        elif choice == "2":
            seperator()
            print(f"{name} goes to the top of an rock, but slips back into the ocean on the top of a large pile ")
            print("of plastic. They get entangled in the plastic and suffocates.")
            ending_get(ending_fact[0][2], ending_fact[1][2])
            menu()
            break
        else:
            print("insert a choice (1 | 2)")

#----------------

def adventure1_path1():
    seperator()
    while True:

        print(f"{name} goes up to the structure, it looks like a oil rig. They are very curious")
        print("and wishes to explore. There is a large black stain on the surface of the ocean around the big")
        print("concreate structure")
        choice = input("1.Explore black stain\n2.Explore concreate structure\n").lower()

        if choice == "1":
            seperator()
            print(f"{name} goes towards the black liquid and it gets stuck on them. They try to swim but")
            print("the oil weights them down, drowning")
            ending_get(ending_fact[0][3], ending_fact[1][3])
            menu()
            break
        elif choice == "2":
            seperator()
            print(f"{name} gets close to the structure and hears some yelling noises along with a sound")
            print("with a bright light above the water. They poke their head above the water to see ")
            print(f"a large flash followed by a explosion, with a large metal debris hitting {name}")
            ending_get(ending_fact[0][4], ending_fact[1][4])
            menu()
            break
        else:
            print("insert a choice (1 | 2)")

# _______
# Main


loading()

menu()
