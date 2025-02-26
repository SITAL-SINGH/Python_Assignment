
# add section
def AddStaff():
        
        while True:
        #info of the person to be added
            name=input("Name: ")
            email=input("Email: ")
            password=input("Password: ")
            Role=input("Role: ")
            data=[name+",",email+",",password+",",Role+"\n"]
            
            # appending the data 
            with open("./Databases/UsersData.txt", "a") as f:
                    f.writelines(data)
   
            # admin to chose
            AdminChoice=input("Continue adding or exit")
            if AdminChoice=="e":
                break
    
        
 # edit section           
def EditStaff():

    # read the data
    with open("./Databases/UsersData.txt", "r") as f:
        lines=f.readlines()
            
    # input for edit
    existing_data=input("Existing Data: ")
    for i in range(len(lines)):
        if existing_data in lines[i]:
            name=input("Name: ")
            email=input("email: ")
            password=input("Password: ")
            role=input("Role: ")
            NewData=f"{name},{email},{password},{role}\n"
            lines[i]=NewData
            break
            
    # writing the new data in the database again
    with open("./Databases/UsersData.txt", "w") as f:
        f.writelines(lines)

# Delete section
def DeleteStaff():
    # first read the data as a list
    with open("./Databases/UsersData.txt", "r") as f:
        lines=f.readlines()
        print(lines)

    # upadated data list
    updated_data=[]

    # data to delete
    existing_data=input("Existing Email: ")

    # Delete the data from the storage
    for line in lines: 
        if existing_data in line: 
            continue
        else:
            updated_data.append(line)

    # write the data again
    with open("./Databases/UsersData.txt", "w") as f:
        f.writelines(updated_data)
           


# operate
def manage():
    print(" Actions: ")
    print("1. Add")
    print("2. Edit")
    print("3. Delete")

    # input for which action to perform
    AdiminAction=input("Choose the action: ")
    if AdiminAction=="add":
        AddStaff()
    
    elif AdiminAction=="edit":
        EditStaff()

    elif AdiminAction=="delete":
        DeleteStaff()

manage()

       



            
            


           

        

        

            
            



