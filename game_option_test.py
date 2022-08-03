
ending_fact = [["Ending: Fish", "Ending: Glass", "Ending: Plastic",
                "Ending: Oiled", "Ending: Boom", ],
               [
            "Fact: Microplastics are fragments of any type of plastic "
            "less than 5 mm in length",
            "Fact: The Great Pacific Garbage Patch is a collection of "
            "marine debris in the North Pacific Ocean.",
            "Fact: Thousands of seabirds and sea turtles, seals and other"
            "marine mammals are killed each year",
            "Fact: Oil spreads over the surface of water in a thin layer"
            "that stops oxygen getting to the wildlife",
            "Fact: Oil  can disrupt animals' communication, breeding and"
            "nesting with loud noises and human movement."],
            [
            "1.Fish 2.Interesting structure", "1.Follow seals 2.Relax",
            "1.Explore black stain 2.Explore concreate"]]




def adventure1():

    print("stars to chase one of the fish. They almost catch it\n"
              f"when they spot a interesting looking structure")
    game_choice(ending_fact[2][0], adventure2(), ending_fact[0][4])

def adventure2():

    print("aaaaaaa")
    game_choice(ending_fact[2][1], ending_fact[0][1], ending_fact[0][4])




def game_choice(option,path1, path2):
    while True:
        choice = input(option).lower()
        if choice == "1":
            print(path1)
            break
        elif choice == "2":
            print(path2)
            break
        else:
            print("insert a choice (1 | 2)")





adventure1()
