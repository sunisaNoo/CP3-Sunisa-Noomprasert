usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "admin":
    print("----- Sunisa Shop -----")
    print("Please Select Choice")
    print("Choice 1 - Nike Price : 15000")
    print("Choice 2 - Adidas Price : 5000")
    print("Choice 3 - Asic Price : 3000")
    userSelected = int(input("--> "))
    if userSelected == 1:
        price = 15000
        unit = int(input("Unit Nike : "))
        result = unit*price
        print(result)
    elif userSelected == 2:
        price = 5000
        unit = int(input("Unit Adidas : "))
        result = unit * price
        print(result)
    elif userSelected == 3:
        price = 3000
        unit = int(input("Unit Asic : "))
        result = unit * price
        print(result)
