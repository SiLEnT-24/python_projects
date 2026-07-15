import random
import string

passwords = {}

# load exiting password file

try:
    with open ("Password.text", "r") as file:
        for line in file :
            website,pwd = line.strip().split(":")
            passwords[website] = pwd

except:
    pass

def generate_password():
      chars = string.ascii_letters+string.digits+"!@#$%&"
      password ="".join(random.choice(chars) for _ in range(8))

while True:
    print("\n-----PASSWORD MANAGER-----")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")
    
    choice = input("Enter your choice:")

    if choice == "1":
        site = input("Enter website:")
        pwd = input("Enter password:")

        passwords[site] = pwd

        with open("Passwords.text", "a")as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved!")

    elif choice == "2":
        if not passwords:
            print("No data")

        else:
            for site, pwd in passwords.items():
                 print(site,":",pwd)

        elif choice == "3":
            print("Generated Password", generate_password())
        
        elif choice == "4":
            print("exit...")
            break

        else:
            print("Invalid input")