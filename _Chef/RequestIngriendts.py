
# add section
def AddIngredients():
        
    while True:
    #info of the person to be added
        name=input("Food Name: ")
        ingredients=input("Ingredients: ")
    
        data=[name+",",ingredients+"\n"]
        
        # appending the data 
        with open("./Databases/Ingredients.txt", "a") as f:
                f.writelines(data)

        # admin to chose
        AdminChoice=input("Continue adding or exit")
        if AdminChoice=="e":
            break
    
        
 # edit section           
def EditIngredients():

    # read the data
    with open("./Databases/Ingredients.txt", "r") as f:
        lines=f.readlines()
            
    # input for edit
    existing_data=input("Existing Food Name: ")
    for i in range(len(lines)):
        if existing_data in lines[i]:
            name=input("Name: ")
            ingredients=input("Ingredients: ")
            
            NewData=f"{name},{ingredients}\n"
            lines[i]=NewData
            break
            
    # writing the new data in the database again
    with open("./Databases/Ingredients.txt", "w") as f:
        f.writelines(lines)


# Delete section
def DeleteIngredients():
    # first read the data as a list
    with open("./Databases/Ingredients.txt", "r") as f:
        lines=f.readlines()
        print(lines)

    # upadated data list
    updated_data=[]

    # data to delete
    existing_data=input("Food Name to be deleted: ")

    # Delete the data from the storage
    for line in lines: 
        if existing_data in line: 
            continue
        else:
            updated_data.append(line)

    # write the data again
    with open("./Databases/Ingredients.txt", "w") as f:
        f.writelines(updated_data)
           


# operate
def manage():
    print(". Actions: ")
    print("1. Add")
    print("2. Edit")
    print("3. Delete")

    # input for which action to perform
    AdiminAction=input("Choose the action: ")
    if AdiminAction=="add":
        AddIngredients()
    
    elif AdiminAction=="edit":
        EditIngredients()

    elif AdiminAction=="delete":
        DeleteIngredients()

manage()

       



            
            


           

        

        

            
            



