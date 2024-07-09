# WRITE A PROGRAM FOR ADDING AND DELETING IN DICTIONARIES.

a={}

def add():
    global a
    topic=input("Topic: ")
    intro=input("Introduction about it: ")
    a[topic]=intro
    print(a)

def delete():
    global a
    delete_choice=input("Enter the topic you want to delete: ")
    a.pop(delete_choice)
    print (a)

def to_do_task():
    while True:
        print('Enter your choice')
        print('1.Add task')
        print ('2.Delete task')
        print('3.Exit')
        a=int(input("Enter your choice: "))
        if a==1:
            add()
        if a==2:
            delete()
        if a==3:
            break
to_do_task()