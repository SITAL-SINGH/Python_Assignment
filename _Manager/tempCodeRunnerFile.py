#info of the person to be added
name=input("Name: ")
email=input("Email: ")
password=input("Password: ")
Role=input("Role: ")
data=[name+",",email+",",password+",",Role+"\n"]

# appending the data 
with open("./Databases/CustomerData.txt", "a") as f:
        f.writelines(data)

# admin to chose
AdminChoice=input("Continue adding or exit")
if AdminChoice=="e":
        break