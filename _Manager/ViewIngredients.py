def ingredients():
    with open("./Databases/Ingredients.txt", "r") as f:
        print(f.read())

def main():
    print("Ingredients: ")
    ingredients()

main()
