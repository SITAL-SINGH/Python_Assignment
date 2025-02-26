import LogIn
email=LogIn.Login()

def role(email): 
    Email=email.lower().strip()
    if "admin" in Email: 
        Role="Admin"
        print(f"Role : {Role}")
    elif "manager" in Email: 
        Role="Manager"
        print(f"Role : {Role}")
    elif "chef" in Email: 
        Role="Chef"
        print(f"Role : {Role}")

print(role)
