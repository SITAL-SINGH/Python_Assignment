


''' allow customer to add, edit and delete order and pay transaction'''
def viewAndOrder():
    def payTransaction(foodName,NoOfServings):
        menuDetails=loadMenu()
        print("Pay Price For Confirmation")
        for item in menuDetails.items():
            if foodName.lower().strip() == item[0]:
                needPrice=int(item[1])*int(NoOfServings)
                print("Price Need To Be Paid: Rs",needPrice )
                while True:
                    payAmount=int(input("Enter Price: "))
                    if payAmount==needPrice:
                        return True
                    else:
                        print("Insufficient amount")
        return False
        
    def loadMenu():
        menuDetails={}
        with open("./Databases/menu.txt", "r") as f: 
            Items=f.readlines()
            for item in Items:
                foodName,price=item.strip().split(",")
                menuDetails[foodName]=price
        return menuDetails

    def viewMenu():
        menuDetail=loadMenu()
        for item in menuDetail.items():
            print(f"Food Name: {item[0]}          Price: Rs {item[1]}")
        

    def orderAdd():
        foodName=input("Food Name: ")
        NoOfServings=int(input("No of Servings: "))
        OrderStatus="in progress".capitalize()
        with open("./Databases/OrderList.txt", "a") as f:
            while True:
                OrderConfirm=payTransaction(foodName,NoOfServings)
                if OrderConfirm==True:
                    f.write(f"{foodName},{NoOfServings},{OrderStatus}\n")
                    print("Ordered Successfully")
                    break
                else:
                    print("Order Unsuccessfull")
        
    def orderEdit():
        ''' load all the orders '''
        with open("./Databases/OrderList.txt" , "r" ) as f:
            orderList=f.readlines()

            
            
    def orderDelete():
        pass


    def CustomerOrder():
        print(''' Actions: 
        1.View Menu
        2. Order food
        3. change food
        4. Cancel ordered food ''')

        try: 
            CustomerChoice= int(input("Action: "))
            match CustomerChoice: 
                case 1: 
                    viewMenu()
                case 2: 
                    orderAdd()
                case 3: 
                    pass
                case 4: 
                    pass
        except:
            print("Invalid Input! please try again!!")

    CustomerOrder()

''' allow customer to view the food status'''
def viewStatus():
    def loadOrder():
        with open("./Databases/OrderList.txt") as file:
            foodStatus={}
            Order_list=file.readlines()
            for line in Order_list:
                foodName,amount,status=line.strip().split(",")
                foodStatus[foodName]=[status,amount]
            return foodStatus
        
    def OrderStatus():
        OrderData=loadOrder()
        for foodName,Details in OrderData.items():
            status,amount=Details
            print(f"Food Name:      {foodName}")
            print(f"Status:         {status}")
            print(f"No of Servings: {amount}\n")

    OrderStatus()

''' allow customer to send feedback '''
def SendFeedBack():
    name= input("Name: ")
    comment= input("Comment: ")

    with open("./Databases/feedback.txt", "a") as f:
        f.write(f"{name},{comment}\n")
        print("Feedback Send Successfull")

''' loads the data of users saved in the database'''
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
            if role=="customer":
                users[username] = [name, password, role]
    return users

''' save the users data if he updated something'''
def save_users(users):
    """Save updated user data back to the file."""
    with open("./Databases/UsersData.txt", "w") as file:
        for username, details in users.items():
            name, password, role = details  # Extract values correctly
            file.write(f"{name},{username},{password},{role}\n")



''' allow customer to update his profile'''
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




''' interface for the customer'''
def main():
    print("Welcome to the Customer Page\n")
    print('''
    Actions: 
    1. View & order food and pay
    2. View order status.
    3. Send feedback
    4. Update own profile.

    ''')
    try: 
        ActionChoice=int(input("Choose the action: "))
        match ActionChoice:
            case 1:
                viewAndOrder()
            case 2:
                viewStatus()
            case 3:
                 SendFeedBack()
                
            case 4:
                update_profile()
    except: 
        print("\nInvalid Input! Please try again")

if __name__=="__main__":
    main()