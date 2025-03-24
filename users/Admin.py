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
                print(f"Skipping malformed line: {line}")  
                continue  
            name, username, password, role = parts
            users[username] = [name, password, role]
    return users


def save_users(users):
    """Save updated user data back to the file."""
    with open("./Databases/UsersData.txt", "w") as file:
        for username, details in users.items():
            name, password, role = details  # Extract values correctly
            file.write(f"{name},{username},{password},{role}\n")
            

''' Include properties of admin to edit, add or delete the staffs'''
def manageStaff():

    """Allows the admin to add a new user."""
    def add_staff():
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
            if role.strip().lower() not in ["customer","manager","chef","admin"]:
                print("Invalid role!!")
            else:
                break

        users[username] = (name,password,role)
        save_users(users)
        print("User added successfully!")

    def editStaff():
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
            users.update({newUsername: users[existEmail]}) # update the username
            del users[existEmail]
            save_users(users)  # Save changes to file
            print("Profile updated successfully!")
            
        else:
            print("User not found.")

    def delete_staff():
        """Allows the admin to delete a user."""
        users = load_users()
        userToDelete = input("Enter username to delete: ")
        if userToDelete in users:
            del users[userToDelete]
            save_users(users)
            print("User deleted successfully!")
        else:
            print("User not found!")
    
    def manage():
        ''' interface for the admin to add , edit or delete the users data'''
        print(" Actions: ")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")
        
        validInputs=("1","2","3","add","edit","delete") #Correct inputs
        # input for which action to perform
        AdiminAction=input("Choose the action: ")
        AdiminAction=AdiminAction.strip().lower()
        if AdiminAction in validInputs:
            if AdiminAction=="add" or AdiminAction=="1":
                add_staff()
            
            elif AdiminAction=="edit" or AdiminAction=="2":
                editStaff()

            elif AdiminAction=="delete" or AdiminAction=="3":
                delete_staff()
        
        else:
            raise("Not valid Action")
    
    manage()

''' Load the orders form OrderList.txt'''
def loadOrder():
    with open("./Databases/OrderList.txt") as file:
        foodStatus={}
        Order_list=file.readlines()
        for line in Order_list:
            orderId,foodName,amount,status,paidAmount,orderDate,completedBy=line.strip().split(",")
            foodStatus[orderId]=[foodName,status,amount,paidAmount,orderDate,completedBy]
        return foodStatus

''' Save the updated orders to OrderList.txt'''    
def SaveOrder(foodlist):
    with open("./Databases/OrderList.txt","w") as f:
        for orderId,Details in foodlist.items():
            foodName,status,amount,paidAmount,orderDate,completedBy=Details
            f.write(f"{orderId},{foodName},{amount},{status},{paidAmount},{orderDate},{completedBy}\n")
        print("Updated Successfully")  

def loadSales():
    """Allows the admin to view sales reports by month or chef."""
    orders = loadOrder()
    
    print("\nSales Report Options:")
    print("1. View sales by month")
    print("2. View sales by chef")
    choice = int(input("Enter your choice: "))
    try: 
        if choice == 1:
            month = input("Enter month (YYYY-MM): ")
            total_sales =0
            for data in orders.values():
                orderMonth=data[4]
                orderPaid=data[3]
                if month==orderMonth:
                    total_sales=int(orderPaid)+total_sales
            print(f"Total sales of month {orderMonth} is {total_sales}")

        elif choice == 2:
            chef_name = input("Enter chef's name: ")
            total_sales=0
            for data in orders.values():
                chefName=data[5]
                orderPaid=data[3]
                if chefName==chef_name:
                    total_sales=int(orderPaid)+total_sales
            print(f"Total sales by chef {chef_name} is {total_sales}")

        else:
            print("Invalid choice!")
    
    except:
        print("Inavalid input!!! please try agaian")




""" allows admin to view the feedback from the customers"""
def loadFeedback():
    print("Feedback Section")
    with open("./Databases/feedback.txt", "r") as file:
        feedbackData=file.readlines()
        for line in feedbackData:
            if line=="\n":
                continue
            name,comment=line.strip().split(",")
            print(f"Name:    {name}")
            print(f"Comment: {comment}\n")

def update_profile():
    """Allow amdin to update their password."""
    users = load_users()
    username=input("Enter Email or Username: ")
    if username in users:
        new_password = input("Enter your new password: ")
        users[username][1] = new_password  # Update the password
        save_users(users)  # Save changes to file
        print("Profile updated successfully!")
    else:
        print("User not found.")

''' Main Interface for admin from which admin can navigate'''
def main():
    print("Welcome to the admin Page\n")
    print('''
    Actions: 
    1. Manage Staff
    2. View Sales Report
    3. View Customer Feedback
    4. Update Profile

    ''')

    try: 
        ActionChoice=int(input("Choose the action: "))
        match ActionChoice:
            case 1:
                manageStaff()
            case 2:
                loadSales()
            case 3:
                loadFeedback()
            case 4:
                update_profile()
    except: 
        print("\nInvalid Input! Please try again")

if __name__=="__main__":
    main()