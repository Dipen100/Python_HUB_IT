# WRITE A PROGRAM FOR CREATING , ADDING AND DELETING IN AN FILE.

def create():
    try:
        file_created=str(input("Enter the file name you want to create: "))
        file=open(file_created,"w")
        a=input("Enter the contans you want to add in it: \n")
        file.write(a+"\n")
        file.close()
    except Exception:
        print("Error! PLEASE TRY AGAIN")

def add():
    file_to_add_text=(input("Enter the file name where you want to add text: "))
    file=open(file_to_add_text,"a")
    added_text=input("Enter the text that you want to add: ")
    file.write(added_text+"\n")
    file.close()

def read():
    try:
        a=input("Enter the file name you want read: ")
        file=open(a,"r")
        print(file.read()+"\n")
        file.close()
    except Exception:
        print("MATCH NOT FOUND: Invalid file name. ")

def delete():
    import os
    try:
        deleting_file=input("Enter the name of the file to delete: ")
        os.remove(deleting_file)
    except Exception:
        print("MATCH NOT FOUND: Invalid file name. ")

def main():
    while True:
        print ("Enter the option you want to do")
        print("1.Create file")
        print("2.Add in file")
        print("3.Read a file")
        print("4.Delete file")
        print("5.Exit")
        input_ask=input("Choice: ")
        if input_ask=="1":
            create()
        if input_ask=="2":
            add()
        if input_ask=="3":
            read()
        if input_ask=="4":
            delete()
        if input_ask=="5":
            break
main()