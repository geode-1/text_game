
import time

# endings system
#list of ending got by player

ending_fact = [["Ending: Fish", "Ending: Glass", "Ending: Plastic", "Ending: Oiled", "Ending: Boom",],
          ["Fact: Microplastics are fragments of any type of plastic less than 5 mm in length",
           "Fact: The Great Pacific Garbage Patch is a collection of marine debris in the North Pacific Ocean.",
           "Fact: Thousands of seabirds and sea turtles, seals and other marine mammals are killed each year",
           "Fact: Oil spreads over the surface of water in a thin layer that stops oxygen getting to the wildlife",
           "Fact: Oil  can disrupt animals' communication, breeding and nesting with loud noises and human movement."
           ]]

endings_list = []


#time delay
def loading():
    for i in range(3):
        time.sleep(0.7)
        print("...")

def ending_get(ending, fact):

    if ending in endings_list:
        global score
        print(ending, fact)
        time.sleep(0.5)
        loading()
        time.sleep(0.5)


    elif ending not in endings_list:
        endings_list.append(ending)
        print(ending)
        print(fact)
        loading()
        time.sleep(0.5)


ending_get(ending_fact[0][0], ending_fact[1][0])
ending_get(ending_fact[0][1], ending_fact[1][1])
ending_get(ending_fact[0][2], ending_fact[1][2])
ending_get(ending_fact[0][3], ending_fact[1][3])
ending_get(ending_fact[0][4], ending_fact[1][4])

print(endings_list)
