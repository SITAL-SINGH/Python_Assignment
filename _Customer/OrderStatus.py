def viewStatus():
    with open("./Databases/OrderList.txt", "r") as f:
        print(f.read())


def main():
    viewStatus()
    


main()