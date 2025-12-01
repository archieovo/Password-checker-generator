import secrets,string,hashlib,requests
from english_words import get_english_words_set 
from numpy import clip
 
def checkStrength():
    userPass = input("\nEnter the password you want to be tested: ")
    length = len(userPass)
    if length < 9:
        score = round(length / 3.0) 
        print(f"\nYour passwords score is {score}" )
    elif length < 16:
        score = round(length / 2.65) 
        print(f"\nYour passwords score is {score}" )
    elif length > 15:
        score = round(length/6.4)
        print(f"\nYour passwords score is {clip(score,7,10)}" )

    if hasBeenBreached(userPass):
        print("\nThis password has been breached")
    else:
        print("\nYour password isn't breached")
    choice = input("\nWould you like to generate a strong password: [y / n]:")
    if choice == "y":
        generatePass()
    elif choice == "n":
        choice2 = input("\nDo you want to test another password? [y / n]:")
        if choice2 == "y":
            checkStrength()

def hasBeenBreached(userPass):
    hashed = hashlib.sha1(userPass.encode())
    userWebHash = hashed.hexdigest().upper()
    response = requests.get(f"https://api.pwnedpasswords.com/range/{userWebHash[:5]}")
    data = response.text
    lines = data.splitlines()
    web_hashes = []

    for line in lines:
        web_hashes.append(line.split(":")[0])

    if userWebHash[5:] in web_hashes:
        return True
    else:
        return False
    
def generatePassphrase():
    wordSet = tuple(get_english_words_set(['web2'], lower=True))
    passPhrase = ""  
    length = int(input("Enter desired amount of words(3-10): "))
    
    if length > 10 or length < 3:
        print("Please enter a number between 3 and 10")
        generatePassphrase()
        return
    
    for i in range(length):
        words = secrets.choice(wordSet)
        passPhrase += words + "_"
    print(passPhrase[:-1])

def generateRandomString():
    characterPool = string.ascii_letters + string.digits + string.punctuation 
    password = ""
    length = int(input("\nEnter desired password length(8-64): "))
    if length > 64 or length < 8:
        print("\nPlease enter a number between 8-64")
        generatePass()
        return
    
    for i in range(length):
        chars = secrets.choice(characterPool)
        password += chars
    print(password)


def generatePass():
    option = int(input("\n1. Series of characters\n2. Passphrase"))
    if option == 1:
        generateRandomString()
    elif option == 2:
        generatePassphrase()
    
