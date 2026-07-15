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
