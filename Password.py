import string
import secrets
want=int(input("Enter 1 for Password Strength and 2 for Strong Password Generation"))

def CheckPassword():
    stre=0
    password=input("Enter Password:")
    L=["123456","1234","12345","abc","ABC"]
    if password in L:
        return "Common Password:Weak"
    if len(password)>=8:
        stre+=1
    if any(j.islower() for j in password):
        stre+=1
    if any(j.isupper() for j in password):
        stre+=1
    if any(j.isdigit() for j in password):
        stre+=1
    if any(j in string.punctuation for j in password):
        stre+=1
    if stre>=4:
        return "Strong Password"
    elif stre>=3 and stre<4:
        return "Medium Password"
    return "Weak Password"

def generate_password():
    length = int(input("Enter length: "))
    if length < 8:
        return "Too short! Use at least 8."
    else:
        pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password = ""
        for c in range(length):
            password += secrets.choice(pool)
        return password

if want==1:
    print(CheckPassword())
if want==2:
    print(generate_password())


