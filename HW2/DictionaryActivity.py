dictSize = int(input("Matrix Size : "))
mydict = {}
print()
for x in range(0, dictSize):
    mydict[x] = input(f"Shopping Item {x+1} : ")

while True:
    ans = input("\nWhat Would you like to do [C]hange items, [R]emove item, [D]isplay items, [S]earch? : ")
    
    if ans == '*':
        print("End of The Program.")
        break

    elif ans == "D" or ans == "d":
        print("KEY - VALUE")
        for x, y in mydict.items():
            print(f"{x} - {y}")

    elif ans == "s" or ans =="S":
        search = input("\nEnter Item to Search : ")
        searching = False

        for x in list(mydict.keys()):
            if search == mydict[x]:
                searching = True
                print(f"Found {search} Item at Key {x}.")
            elif search.isdigit() and int(search) == x:
                searching = True
                print(f"{search} Contains {mydict[x]}.")
        if searching == False:
            print(f"I'm sorry, {search} NOT in the Cart.")

    elif ans == "R" or ans == "r":
        remove = input("\nEnter Item to Remove : ")
        removing = False
            
        for x in list(mydict.keys()):
            if remove == mydict[x]:
                removing = True
                print(f"The Key {x} with the Value of {mydict[x]} has been Deleted.")
                mydict.pop(x)
                break
            elif remove.isdigit() and int(remove) == x:
                removing = True
                print(f"The Key {remove} with the Value of {mydict[x]} has been Deleted.")
                mydict.pop(x)
                break
        if removing == False:
            print(f"I'm sorry, {remove} NOT in the Cart.")
    
    elif ans == "c" or ans == "C":
        change = input("\nEnter Key to Change : ")
        changing = False
        for x in list(mydict.keys()):
            
            if change.isdigit() and int(change) == x:
                changing = True
                mydict[x] = input(f"Enter New Value for {x} : ")
                break
            elif change == mydict[x]:
                changing = True
                mydict[x] = input(f"Enter New Value for {x} : ")
                break
        if changing == False:
            print(f"{change} Key Not Found.")

    else:
        print("Try Again.")
