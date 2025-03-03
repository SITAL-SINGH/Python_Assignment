
''' Load users Data from the Database or UsersData.txt file'''
def load_users():
    """Load users from the text file into a dictionary."""
    users = {}
   
    with open("./Databases/UsersData.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue  
            parts = line.split(",")
            if len(parts) != 4:  # Ensure exactly 4 values
                print(f"⚠️ Skipping malformed line: {line}")  
                continue  
            name, username, password, role = parts
            if role in ["manager","customer"]:
                users[username] = [name, password, role]
            
    return users

''' save users Data in the Database or UsersData.txt file'''
def save_users(users):
    """Save updated user data back to the file."""
    with open("./Databases/UsersData.txt", "w") as file:
        for username, details in users.items():
            name, password, role = details  # Extract values correctly
            file.write(f"{name},{username},{password},{role}\n")

''' properties for manager to add, edit or delete the customer'''
def ManageCustomer():

    """Allows the admin to add a new user."""
    def add_Customer():
        users = load_users()
        name=input("Name: ")

        while True: 
            username = input("Enter new username: ")
            if username in users:
                print("Username already exists!")
            else:
                break
        password = input("Enter password: ")
        while True:
            role = input("Enter role (Admin/Manager/Chef/Customer): ")
            if role.strip().lower() not in ["customer"]:
                print("Invalid role!!")
            else:
                break

        users[username] = (name,password,role)
        save_users(users)
        print("User added successfully!")

    def editCustomer():
        """Allows the admin to add a edit user profile."""
        users = load_users()
        existEmail=input("Existing Username/Email: ")
        if existEmail in users:
            name=input("New Name: ")
            newUsername=input("New Email/Username: ")
            new_password = input("Enter your new password: ")
            role = input("Enter role (Admin/Manager/Chef/Customer): ")
        
            users[existEmail][0] = name  # Update the name
            users[existEmail][1] = new_password  # Update the password
            users[existEmail][2] = role  # Update the role
            users[existEmail] = newUsername  # Update the email or password
            save_users(users)  # Save changes to file
            print("✅ Profile updated successfully!")
            
        else:
            print("❌ User not found.")

    def delete_Customer():
        """Allows the admin to delete a user."""
        users = load_users()
        username = input("Enter username to delete: ")
        if username in users:
            del users[username]
            save_users(users)
            print("User deleted successfully!")
        else:
            print("User not found!")

    def manage():
        print(" Actions: ")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")

        validInputs=("add","edit","delete","1","2","3")
        # input for which action to perform
        AdiminAction=input("Choose the action: ")
        AdiminAction=AdiminAction.strip().lower()
        if AdiminAction in validInputs:
            if AdiminAction=="add" or AdiminAction=="1" :
                add_Customer()
            
            elif AdiminAction=="edit" or AdiminAction=="2" :
                editCustomer()

            elif AdiminAction=="delete" or AdiminAction=="3" :
                delete_Customer()
        else:
            print("invalid Action")


    manage()

''' properties of manager to add , delete or edit items in menu'''
def ManageMenu():

    def loadMenu():
        menuList={}
        with open("./Databases/menu.txt", "r") as f:
            menuData=f.readlines()
            for line in menuData:
                foodName,price=line.strip().split(",")
                menuList[foodName]=price
        return menuList
    
    def saveMenu(menuData):
        """Save updated menu back to the file."""
        with open("./Databases/menu.txt", "w") as file:
            for foodName, price in menuData.items():
                file.write(f"{foodName},{price}\n")
    
    def AddItem():
        ''' allow food to added in the menu'''
        menuData=loadMenu()
        while True:
            foodName=input("Food Name: ")
            if foodName in menuData:
                print(f"{foodName} already exist in menu")
            else:
                break
        price=input("Price: ")
        # appending the data in menuData
        menuData[foodName]=price

    def editMenu():
        """Allows the manager to edit Menu items."""
        menuData = loadMenu()
        existFood=input("Existing Food Name: ")
        if existFood in menuData:
            price=input("New Price: ")
        
            menuData[existFood] = price  # Update the price of the food
            saveMenu(menuData)  # Save changes to file
            print("✅ Profile updated successfully!")
            
        else:
            print("❌ User not found.")

    def deleteMenu():
        """Allows the admin to delete a user."""
        menuData = loadMenu()
        existfood = input("Enter foodName that you want to delete: ")
        if existfood in menuData:
            del menuData[existfood]
            save_users(menuData)
            print("User deleted successfully!")
        else:
            print("User not found!")

    def manage():
        print(" Actions: ")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")
        
        validInputs=("add","edit","delete","1","2","3")
        # input for which action to perform
        AdiminAction=input("Choose the action: ")
        AdiminAction=AdiminAction.strip().lower()
        if AdiminAction in validInputs:
            if AdiminAction=="add" or AdiminAction=="1":
                AddItem()
            
            elif AdiminAction=="edit" or AdiminAction=="2":
                editMenu()

            elif AdiminAction=="delete" or AdiminAction=="3":
                deleteMenu()
        else:
            print("Invalid Action!!")


    manage()

def viewIngredients():
    with open("./Databases/Ingredients.txt", "r") as f:
        data=f.readlines()
        for line in data:
            foodName,Ingredients=line.strip().split(":")
            Ingredients=Ingredients.split(",")
            print(f"Food Name: {foodName}")
            print("Ingredients: ")
            for index,item in enumerate(Ingredients,start=1):
                print(f"{index} : {item}")
            print("\n")


def update_profile():
    """Allow user to update their password."""
    users = load_users()
    username=input("Enter existing Email or Username: ")
    if username in users:
        new_password = input("Enter your new password: ")
        users[username][1] = new_password  # Update the password
        save_users(users)  # Save changes to file
        print("✅ Profile updated successfully!")
    else:
        print("❌ User not found.")


def main():
    print("Welcome to the admin Page\n")
    print('''
    Actions: 
    1. Manage Customer
    2. Manage menu categories and pricing
    3. View ingredients
    4. Update Profile

    ''')
    try: 
        ActionChoice=int(input("Choose the action: "))
        match ActionChoice:
            case 1:
                ManageCustomer()
            case 2:
               ManageMenu()
            case 3:
                viewIngredients()
            case 4:
                update_profile()
    except: 
        print("\nInvalid Input! Please try again")
if __name__=="__main__":
    main()