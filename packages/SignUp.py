USER_FILE = "./Databases/UsersData.txt"

def is_username_taken(username):
    """Checks if the username already exists in the file."""
    
    with open(USER_FILE, "r") as file:
        data=file.readlines()
        for line in data:
            name,Username,password,role=line.strip().split(",")
            if Username == username:
                return True
    return False

def sign_up():
    """Allows a new user to sign up and saves credentials to a file."""
    name = input("Enter your full name: ").strip()

    while True:
        username = input("Choose a username: ").strip()
        if is_username_taken(username):
            print("Username already taken. Try another one.")
        else:
            break

    password = input("Enter password: ").strip() # Hashing the password

    role ="customer"

    with open(USER_FILE, "a") as file:
        file.write(f"{name},{username},{password},{role}\n")

    print("Sign-up successful!")
    return role,username

if __name__ == "__main__":
    role,username=sign_up()
