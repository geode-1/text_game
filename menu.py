
import time

#time delay
def loading():
    for i in range(3):
        time.sleep(0.7)
        print("...")


# menu system

def play_menu():
    print("=====" * 34)
    while True:
        choice = input("""
    1. Play game
    2. Total endings
    3. Quit
    4. Reset data
        """)
        if choice == "1":
            print(adventure_start())
            break
        elif choice == "3":
            print("Thank you for playing the game")
            break
        else:
            print("Enter a valid option")



def adventure_start():
    print("=====" * 34)
    print("Test take back menu")
    choice = input("go back to menu? (y/n)")
    if choice == "y":
        try:
            loading()
            time.sleep(0.7)
            play_menu()
        except:
            print("ops")
    else:
        print("ok")


play_menu()