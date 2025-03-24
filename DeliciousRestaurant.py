from packages import LogIn
from packages import SignUp
from users import Admin
from users import Chef
from users import Manager
from users import Customer


''' redirect to the page according to role'''
def redirect(role):
    if role == "admin":
        Admin.main()
    elif role == "manager":
        Manager.main()
    elif role == "chef":
        Chef.main()
    elif role == "customer":
        Customer.main()

''' Main Interface when opening the app'''
def main():
    print("Welcome to Delicious Restaurant Management System!\n")

    print("1. Log In" )
    print("2. Sign up")
    choice=int(input("Choice(1/2): "))
    if choice== 1:
        role,username=LogIn.authenticate()
        print(role)
        redirect(role)

    elif choice ==2:
        role,username=SignUp.sign_up()
        redirect(role)

main() # calling the function
        
    