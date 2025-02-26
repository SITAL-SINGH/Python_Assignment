def AdminAction():
    print('''
        1. Manage Staff
        2. View Sales Report
        3. View Customer Feedback
        4. Update Profile

        ''')

def main():
    print("Welcome to the admin Page\n")
    print("Actions: ")
    AdminAction()

    ActionChoice=input("Choose the action: ")
    match ActionChoice:
        case "m":
            pass
        case "s":
            pass
        case "c":
            pass
        case "u":
            pass






main()



