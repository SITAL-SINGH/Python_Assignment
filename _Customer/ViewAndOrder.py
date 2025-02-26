def viewMenu():
    with open("./Databases/menu.txt", "r") as f: 
        Items=f.read()
        print(Items)
        # for item in Items: 
        #     print(item)

def orderAdd():
    item=input("Food Name: ")
    with open("./Databases/OrderList.txt", "a") as f:
        f.write(f"Food Name: {item} ")

def orderEdit():
   pass
def orderDelete():
    pass


def main():
    print(''' Actions: 
    1. Add
    2. Edit
    3. Delete ''')

    CustomerChoice= input("Action: ")
    match CustomerChoice: 
        case "add": 
            pass
        case "edit": 
            pass
        case "delete": 
            pass
  







    orderAdd()


main()
