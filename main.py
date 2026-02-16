from emp import create,read,update,delete,search

while True:
    print("1. to ADD Employee details")
    print("2. to DISPLAY all Employee details")
    print("3. to UPDATE an Employee's Details")
    print("4. to DELETE an Employee's Details")
    print("5. to SEARCH an Employee's Details")
    print("6. to EXIT")
    ch=input("Enter your Choice")

    if ch=="1":
        print("You have selected to CREATE New Employee details:")
        create()
    elif ch=="2":
        print("You selected to PRINT All Employee details: ")
        read()
    elif ch=="3":
        print("You selected to UPDATE Employee details: ")
        update()
    elif ch=="4":
        print("You selected to DELETE Employee details: ")
        delete()
    elif ch=="5":
        print("You selected to SEARCH Employee details: ")
        search()
    elif ch=="6":
        print("Closing")
        break
    else:
        print("Invalid Choice")
        break