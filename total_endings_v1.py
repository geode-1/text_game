
import time

# endings system
endings = []

#time delay
def loading():
    for i in range(3):
        time.sleep(0.7)
        print("...")


def ending_get(ending):
    while True:
        choice = input("Press 1 to test receive ending, press 2 to test receive ending already gotten ")
        if choice == "1":
            endings.append(ending)
            break
        elif choice == "2":
            print("????")
            break
        else:
            print("Please respond as stated")


ending_get("Ending: Oiled")
ending_get("Ending: Ouch")
ending_get("Ending: WOW")
ending_get("Ending: mo")

print(endings)

