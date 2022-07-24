
import time

def loading():
    for i in range(3):
        time.sleep(0.7)
        print("...")


#  deletion system
endings = ["Ending: Oiled", "Ending: Ouch", "Ending: WOW", "Ending: mo"]
print(endings)

def ending_delete():
    while True:
        choice = input("Are you sure to delete your data? (y/n)")
        if choice == "y":
            loading()
            endings.clear()
            time.sleep(0.7)
            print("Done! Data deleted")
            print(endings)
            break
        elif choice == "n":
            print("Ok, we will go back to the menu instead")
            break
        else:
            print("Please respond with (y/ n)")


ending_delete()
