def feedBack():
    name= input("Name: ")
    comment= input("Comment: ")

    with open("./Databases/feedback.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Comment: {comment}\n")
        f.write("\n")


feedBack()