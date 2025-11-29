# Import utils' functions here to use
from utils import generatePass, checkStrength

def main():
    option: int

    try:
        option = int(input("1. Generate password\n2. Check Password\n"))

        if option not in [1,2]:
            print("Invalid option.")
            return
    except ValueError:
        print("Invalid option.")
        return

    if option == 2:
        checkStrength()
    elif option == 1:
        generatePass()



if __name__ == "__main__":
    main()