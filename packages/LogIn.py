USER_FILE = "./Databases/UsersData.txt"


def load_users():
    """Load users from the text file into a dictionary."""
    users = {}

    with open(USER_FILE, "r") as file:
        Data=file.readlines()
        for line in Data:
            name,username,password,role = line.strip().split(",")
            users[username] = (password.strip(), role.strip(), name.strip())

    return users

def authenticate():
    """Authenticate user with three login attempts."""
    users = load_users()
    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and password==users[username][0]:
            print(f"Login successful! Welcome, {username}. Role: {users[username][1]}")
            return users[username][1], username  # Return role and username

        else:
            print("Invalid username or password. Try again.")
            attempts += 1

    print("Maximum login attempts reached. Exiting...")
    return None, None

if __name__ == "__main__":

    role, user = authenticate()
    if role:
        print(f"Access granted for {role} account.")
    else:
        print("Access denied.")