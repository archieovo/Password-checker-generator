import secrets,string,wordlist



def checkStrength():
    return

def generatePassphrase():
    return

def generateRandomString():
    characterPool = string.ascii_letters + string.digits + string.punctuation 
    password = ""
    length = int(input("Enter desired password length(8-64): "))
    if length > 64 or length < 8:
        print("Please enter a number between 8-64")
        generatePass()
        return
    
    for i in range(length):
        chars = secrets.choice(characterPool)
        password += chars
    print(password)


def generatePass():
    option = int(input("1. Series of characters\n2. Passphrase"))
    if option == 1:
        generateRandomString()
    elif option == 2:
        return
    
