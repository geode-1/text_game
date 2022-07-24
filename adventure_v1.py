

#Start
def adventure_start():
    print("====="*34)
    global name
    name = input("what is your name?\n")
    while True:

        print("{} is a seal, they wander in the ocean and encounter a school of fish to their left".format(name))
        print("and other seals to their right ")
        choice = input("1.Left \n2.Right\n")

        if choice == "1":
            print(adventure1())
            break

        elif choice == "2":
            print(adventure2())
            break

        else:
            print ("insert a choice (1 | 2)")

#-----

def adventure1():
    print("=====" * 34)
    while True:

        print("{} stars to chase one of the fish. They almost catch it when they spot a interesting".format(name))
        choice = input(" looking structure.\n1. Fish \n2. Interesting structure \n")
        if choice == "1":
            print("You manage to catch and eat the fish, but oh no!! The fish was filed")
            print("with chunks of plastic. You choke and die.")
            print("Ending: Fish")
            #take back to menu
            break

        elif choice == "2":
            print(adventure1_path1())
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
            print(f"They follow the other seals, {name} slowly hops on the sand until suddenly they ")
            print(f"feels a sarp pain on them. Sharp pieces of glass from bottles have stabbed the {name}'s stomach")
            print("causing them to eventually bleed to death")
            print("Ending:  ")
            break
        elif choice == "2":
            print (adventure2_path2())
            break
        else:
            print("insert a choice (1 | 2)")

#-----

def adventure2_path2():
    print("=====" * 34)
    while True:

        choice = input("1.dd \n2.ddd \n")

        if choice == "1":
            print("Ending:  ")
            break
        elif choice == "2":
            print("Ending:  ")
            break
        else:
            print("insert a choice (1 | 2)")

def adventure1_path1():
    print("=====" * 34)
    while True:

        print(f"{name} goes up to the structure, it looks like a oil rig. They are very curious")
        print("and wishes to explore. There is a large black stain on the surface of the ocean around the big")
        print("concreate structure")
        choice = input("1.Explore black stain\n2.Explore concreate structure\n")

        if choice == "1":
            print(f"{name} goes towards the black liquid and it gets stuck on them. They try to swim but")
            print("the oil weights them down, drowning")
            #ending_get("Ending: Oiled")
            print("Ending: Oiled")
            break
        elif choice == "2":
            print(f"{name} gets close to the structure and hears some yelling noises along with a sound")
            print("with a bright light above the water. They poke their head above the water to see ")
            print(f"a large flash followed by a explosion, with a large metal debris hitting {name}")
            # ending_get("Ending: Boom")
            print("Ending: Boom ")
            break
        else:
            print("insert a choice (1 | 2)")



adventure_start()