
import time

# endings system
#list of ending got by player
endings_list = ["Ending: WOW"]


#time delay
def loading():
    for i in range(3):
        time.sleep(0.7)
        print("...")


def ending_get(ending):

    if ending == endings_list:
        print("Ending got:", ending)

    elif ending not in endings_list:
        endings_list.append(ending)
        print("Ending got:", ending)


ending_get("Ending: Oiled")
ending_get("Ending: Ouch")
ending_get("Ending: WOW")
ending_get("Ending: mo")

print(endings_list)
