import datetime
import random

''' load the order data from OrderList.txt file'''
def loadOrder():
    with open("./Databases/OrderList.txt") as file:
        OrderItem={}
        Order_list=file.readlines()
        for line in Order_list:
            orderId,foodName,amount,status,paidAmount,orderDate,chefName=line.strip().split(",")
            OrderItem[orderId]=[foodName,status,amount,paidAmount,orderDate,chefName]
        return OrderItem

''' save the updated order data '''  
def saveOrder(orderList):
    with open("./Databases/OrderList.txt","w") as f:
        for orderId,Details in orderList.items():
            foodName,status,amount,paidAmount,orderDate,chefName=Details
            f.write(f"{orderId},{foodName},{amount},{status},{paidAmount},{orderDate},{chefName}\n")


''' allow customer to add, edit and delete order and pay transaction'''
def viewAndOrder():
    ''' Confirm order by transaction'''
    def payTransaction(foodName,menuItems,NoOfServings):
        print("Pay Price For Confirmation")
        for item in menuItems.items():
            if foodName.lower().strip() == item[0]:
                needPrice=int(item[1])*int(NoOfServings)
                print("Price Need To Be Paid: Rs",needPrice )
                while True:
                    payAmount=int(input("Enter Price: "))
                    if payAmount==needPrice:
                        return [True,payAmount]
                    else:
                        print("Insufficient amount")
        return False

    ''' load the menu section'''  
    def loadMenu():
        menuDetails={}
        with open("./Databases/menu.txt", "r") as f: 
            Items=f.readlines()
            for item in Items:
                foodName,price=item.strip().split(",")
                menuDetails[foodName]=price
        return menuDetails
    
    ''' all customer to view menu'''
    def viewMenu():
        menuDetail=loadMenu()
        for item in menuDetail.items():
            print(f"Food Name: {item[0]}          Price: Rs {item[1]}")
        
    ''' allow customer to add the order'''
    def orderAdd():
        menuItems=loadMenu()
        ''' calling menu function to show menu'''
        viewMenu

        while True:
            foodName=input("Food Name: ")
            if foodName.strip().lower() not in menuItems:
                print(f"{foodName} not available")
            else: 
                break
            # foodNames=foodNames.split(",")
            # orderedFood={}
            # for food in foodNames:
            #     if food.strip().lower() not in menuItems:
            #         print(f"{food} not available")
            #     else: 
            #         NoOfServings=int(input("No of Servings: "))
            #         orderedFood[food]=NoOfServings    # stores in orderedFood
            
            # if not orderedFood:
            #     print("No valid items selected. Please try again.")
            #     continue  
        NoOfServings=int(input("No of Servings: "))
        OrderStatus="in progress".capitalize()
        ''' choice for user to proceed or cancel the order'''
        choice=input("Do you to confirm the order(yes/no): ")

        if choice.strip().lower()=="yes":
            with open("./Databases/OrderList.txt", "a") as f:
                while True:
                    OrderConfirm,paidAmount=payTransaction(foodName,menuItems,NoOfServings)
                    if OrderConfirm==True:
                        orderDate=datetime.date.today().strftime("%Y-%m") 
                        orderId=random.randint(1,10000)
                        completedBy=""
                        f.write(f"{orderId},{foodName},{NoOfServings},{OrderStatus},{paidAmount},{orderDate},{completedBy}\n")
                        print(f"Ordered Successfully. Your order id is{orderId}")
                        break
                    else:
                        print("Order Unsuccessfull")
        if choice.strip().lower()=="no":
            print("order is cancelled")

    ''' allow customer to edit the order'''   
    def orderEdit():
        ''' load all the orders '''
        orderList=loadOrder()

        ''' order id to edit'''
        orderId=int(input("Enter Order id: "))
        if orderId in orderList:
            foodName=input("enter the food Name: ")
            noOfServings=int("No of Servings: ")
            orderList[orderId][0]=foodName  #changes the food name of the ordered item
            orderList[orderId][2]=noOfServings # changes the number of servings

            saveOrder(orderList) # calling saveOrder function to save the changes
            print("Order Edited successfully")
        else:
            print("order not found")

    ''' allow customer to delete the order placed'''    
    def orderDelete():
        orderList=loadOrder()

        orderId = input("Enter order id to delete: ")
        if  orderId in orderList:
            del orderList[orderId]
            saveOrder(orderList)
            print("User deleted successfully!")
        else:
            print("User not found!")

    ''' Interface for customer to navigate'''
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
                    orderEdit()
                case 4: 
                    orderDelete()
        except:
            print("Invalid Input! please try again!!")


    CustomerOrder()



        
''' allow customer to view the food status'''
def OrderStatus():
    OrderData=loadOrder()

    orderid=input("enter order id to check status: ")
    if orderid in OrderData:
        for orderId,Details in OrderData.items():
            foodName,status,amount,paidAmount,orderDate,chefName=Details
            if orderid==orderId:
                print(f"Food Name:      {OrderData[orderid][0]}")
                print(f"Status:         {OrderData[orderid][1]}")
                print(f"No of Servings: {OrderData[orderid][2]}\n")
                break
    else:
        print("Order not found")


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
                print(f"Skipping malformed line: {line}")  
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



''' allow customer to update his profile password'''
def update_profile():
    """Allow user to update their password."""
    users = load_users()
    username=input("Enter Email or Username: ")
    if username in users:
        new_password = input("Enter your new password: ")
        users[username][1] = new_password  # Update the password
        save_users(users)  # Save changes to file
        print("Profile updated successfully!")
    else:
        print(" User not found.")




''' interface for the customer for navigation'''
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
                OrderStatus()
            case 3:
                 SendFeedBack()
                
            case 4:
                update_profile()
    except: 
        print("\nInvalid Input! Please try again")

if __name__=="__main__":
    main()