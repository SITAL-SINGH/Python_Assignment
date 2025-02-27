


def Login():

    # password and emails for Admins,manager
    user={
        "admin": ["admin123", "admin"],
        "manager": ["manager123", "manager"],
        "chef": ["chef123", "chef"],
        "customer": ["customer123", "customer"]
    }
    

    # input Email and Password
    email=input("Email: ")
    password=input("Password: ")
    
    # user attempts if password is failed
    attempt=1
    max_attempts=3
    
    while attempt<=max_attempts: 
        if email in user and password in user[email]:
           
            print("redirection the related page")
            break

        elif email not in user and password not in user[email]:
            print("Incorret credentials! Please try again....")

        attempt+=1

    if attempt>=3: 
        print("To many attempts account is blocked")

if __name__=='__main__': 
    Login()














