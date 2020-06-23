import sys
placeHolder = 0
datePlaceHolder = 8
holder3 =""
print("Hello I am an APA creater and i will need some information inorder to create it")
try:
    date = input("Please enter the date last edited in MMDDYYYY Format: ")
    if len(date)!= datePlaceHolder:
        print("please enter the correct format")
        sys.exit(0)
    if int(date[0:2])> 12 or int(date[0:2])<= 0:
        print("please enter the correct month")
        sys.exit(0)
    if int(date[2:4])> 31 or int(date[2:4])<= 0:
        print("please enter the correct date")
        sys.exit(0)
    if int(date[4:8])<= 0:
        print("please enter the correct year")
        sys.exit(0)
    if int(date[0:2])== 1:
        date1 = "January"
    elif int(date[0:2]) == 2:
        date1 = "February"
    elif int(date[0:2])== 3:
        date1 = "March"
    elif int(date[0:2])== 4:
        date1 = "April"
    elif int(date[0:2])== 5:
        date1 = "May"
    elif int(date[0:2])== 6:
        date1 = "June"
    elif int(date[0:2])== 7:
        date1 = "July"
    elif int(date[0:2])== 8:
        date1 = "August"
    elif int(date[0:2])== 9:
        date1 = "September"
    elif int(date[0:2])== 10:
        date1 = "October"
    elif int(date[0:2])== 11:
        date1 = "November" 
    elif int(date[0:2])== 12:
        date1 = "December"
    numberOfAuthors = int(input("Please enter the number of authors "))
    while placeHolder < numberOfAuthors:
        firstName = str(input("Please enter the authors first names: "))
        lastName = str(input("Please enter the authors last names: "))
        if str(firstName).isalpha() == False:
            print("Please enter a valid First name")
            sys.exit(0)
        if str(lastName).isalpha() == False:
            print("Please enter a valid Last name")
            sys.exit(0)
        holder2 = lastName + "," + firstName[0]
        if numberOfAuthors > 1:
            holder = ".,"
            holder3 = holder2 + holder + holder3
        else:
            holder3 = holder2 + holder3
        placeHolder += 1
    title = input("Please enter the title name ")
    where = input("please enter where you retrieve this source ")
except:
    print("that is not a valid input")
    sys.exit(0)
print("Printing APA FORMATING PLEASE WAIT")


print( holder3 + "(" + date[4:8] +"," + date1 + " " + date[2:4] + ")" + title + " Retrieved from " + where)
leave = input("Press enter to exit")
