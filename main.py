# Import utils' functions here to use

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
    
        


if __name__ == "__main__":
    main()