def viewOrder():
    with open("./Databases/OrderList.txt" , "r" ) as f:
        print(f.read())


def main():
    print("Order List: ")
    viewOrder()


main()