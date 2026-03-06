# making to-do list a begineer project:- 
tasks=[]
while True:
    print("------------------------------------")
    print("🦋 Welcome To-Do List Application")
    print("------------------------------------")
    print("Enter Your Choice💻: ")
    print("1)  Add Task")
    print("2)  View Tasks")
    print("3)  Mark Task as Completed ✅")
    print("4)  Exit")        
    print("-----------------------------")

    choice =  input("enter your choice: ")

    if choice == "1":
        task = input("enter task: ")
        tasks.append(task)

    elif choice == "2":
        if not tasks:
            print("no task found 🙌")
        else:
            for i in range(len(tasks)):
                print(i + 1,")", tasks[i])  # i+1 is for counting

    elif choice == "3":
        n = int(input("enter task number to mark as completed: "))
        tasks.pop(n-1)
        print("tasks is marked as completed!😁")

    elif choice == "4":
        break 





    
    





