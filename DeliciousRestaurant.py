from Packages import LogIn
from Packages import signUp
def main():
    print("Welcome to Delicious Restaurant Management System!\n")

    print("1. Log In" )
    print("2. Sign up")
    choice=int(input("Choice(1/2): "))
    if choice== 1:
        LogIn.authenticate()

    elif choice ==2:
        signUp.sign_up()

main()
        
    


#     if role == "Admin":
#         while True:
#             print("\nAdmin Menu: 1. Manage Staff 2. View Feedback 3. Logout")
#             if input("Enter choice: ") == "1": manage_staff()
#             elif input() == "2": view_feedback()
#             else: break
#     elif role == "Manager":
#         manage_menu()
#     elif role == "Chef":
#         while True:
#             print("\nChef Menu: 1. View Orders 2. Update Order Status 3. Logout")
#             if input("Enter choice: ") == "1": view_orders()
#             elif input() == "2": update_order_status()
#             else: break
#     elif role == "Customer":
#         while True:
#             print("\nCustomer Menu: 1. Order Food 2. Send Feedback 3. Logout")
#             if input("Enter choice: ") == "1": place_order()
#             elif input() == "2": send_feedback()
#             else: break
#     else:
#         print("Exiting system...")

# if __name__ == "__main__":
#     main()
