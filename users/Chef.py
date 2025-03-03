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
            if role=="chef":
                users[username] = [name, password, role]
    return users

def save_users(users):
    """Save updated user data back to the file."""
    with open("./Databases/UsersData.txt", "w") as file:
        for username, details in users.items():
            name, password, role = details  # Extract values correctly
            file.write(f"{name},{username},{password},{role}\n")

def loadOrder():
    with open("./Databases/OrderList.txt") as file:
        foodStatus={}
        Order_list=file.readlines()
        for line in Order_list:
            foodName,amount,status=line.strip().split(",")
            foodStatus[foodName]=[status,amount]
        return foodStatus
    
def SaveOrder(foodlist):
    with open("./Databases/OrderList.txt","w") as f:
        for foodName,Details in foodlist.items():
            status,amount=Details
            f.write(f"{foodName},{amount},{status}\n")
        print("Updated Successfully")

def loadIngredients():
    
    IngredientsData={}
        # read the data
    with open("./Databases/Ingredients.txt", "r") as f:
        data=f.readlines()
        for line in data:
            foodName,Ingredients=line.strip().split(":")
            IngredientsData[foodName]=Ingredients

    return IngredientsData

def SaveIngredients(IngredientData):
    with open("./Databases/Ingredients.txt","w") as f:
        for foodName,Ingredients in IngredientData.items():
            f.write(f"{foodName}:{Ingredients}\n")
        print("Updated Successfully")



def viewOrder():
    Orders=loadOrder()
    for foodName,Details in Orders.items():
        status,amount=Details
        print(f"food Name:       {foodName} ")
        print(f"No of Serivings: {amount}")
        print(f"Food Status:     {status}\n")
        
        


def updateOrder():
    foodList=loadOrder()
    print(foodList)
    ValidStatus=["in progress", "completed"]
    foodName=input("Food Name: ")
    foodStatus=input("Update FoodStatus: ")
    if foodStatus.lower().strip() not in ValidStatus:
        print("Invalid input")
    else:
        foodList[foodName][0]=foodStatus
        SaveOrder(foodList)


def requestIngredients():
    """Allows the admin to add a new user."""
    def AddIngredients():
        foodName=input("Name: ")
        Ingredients=input("Ingredients: ")
        with open("./Databases/Ingredients.txt", "a") as f:
            f.write(f"{foodName}:{Ingredients}")
            print("Ingredients Added Successfully!!")

        
    def  EditIngredients():
        """Allows the chef to add a edit Ingredients data."""

        IngredientData = loadIngredients()
        existFood=input("Existing FoodName: ")
        if existFood in IngredientData:
            Ingredients=input("New Ingredients: ")
            IngredientData[existFood] = Ingredients  # Update the name
            SaveIngredients(IngredientData)  # Save changes to file
            print("✅ Profile updated successfully!")
            
        else:
            print("❌ User not found.")



    def DeleteIngredients():
        """Allows the admin to delete a user."""
        IngredientsData = loadIngredients()
        foodName = input("Enter foodName that you want to delete: ")
        if foodName in IngredientsData:
            del IngredientsData[foodName]
            save_users(IngredientsData)
            print("User deleted successfully!")
        else:
            print("User not found!")

    def manage():
        print(". Actions: ")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")

        validInputs=("1","2","3","add","edit","delete")
        # input for which action to perform
        AdiminAction=input("Choose the action: ")
        if AdiminAction in validInputs:
            if AdiminAction=="add" or AdiminAction=="1" :
                AddIngredients()
            
            elif AdiminAction=="edit" or AdiminAction=="2":
                EditIngredients()

            elif AdiminAction=="delete" or AdiminAction=="3":
                DeleteIngredients()
        else:
            raise("Not valid Action")
        
    manage()
    
def update_profile():
    """Allow user to update their password."""
    users = load_users()
    username=input("Enter Email or Username: ")
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
        1. View orders placed by customers
        2. Update orders
        3. Request ingredients
        4. Update own profile.

        ''')

    try: 
        ActionChoice=int(input("Choose the action: \n"))
        match ActionChoice:
            case 1:
                viewOrder()
            case 2:
                updateOrder()
            case 3:
                requestIngredients()
                
            case 4:
                update_profile()
    except: 
        print("\nInvalid Input! Please try again")

if __name__=="__main__":
    main()







