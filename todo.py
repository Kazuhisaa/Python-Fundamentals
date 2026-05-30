
things_to_do = []#imbakan ng todo list or ng mga gagawin

def addTasks():
    tasks = (input("What is the task you want to do? \n"))
    things_to_do.append(tasks)
    print ("Succesfully Added!")

def viewTasks():
    for number, item in enumerate(things_to_do,start=1):
        print(f"{number}.{item}")

def markAsDone():
    for number, item in enumerate(things_to_do,start=1):
        print(f"{number}.{item}")
    choose = int(input("Choose the number of thing that you are done.\n"))
    index = choose - 1 
    tasks = things_to_do[index]
    modified_tasks = tasks + (" DONE")
    things_to_do[index] = modified_tasks
    print("Task Marked As Done")

def removeTasks():
    for number, item in enumerate(things_to_do,start=1):
        print(f"{number}.{item}")
    choose = int(input("Choose the number of thing you want to remove.\n"))
    index = choose - 1
    things_to_do.pop(index)
    print("Tasks is Removed!")
    


    

if __name__ == "__main__":
    while True:
        print ("=================")
        print ("     TODO APP    ")
        print ("=================")
        print("\n1. Add To Do ")
        print("2. View To Do")
        print("3. Mark as Done")
        print("4. Remove To Do")
        print("5. Exit")
        choice = int(input("Please choose a number: " ))

        if choice == 1: 
            addTasks()
        elif choice == 2:
            viewTasks()
        elif choice == 3:
            markAsDone()
        elif choice == 4:
            removeTasks()
        elif choice == 5:
            break

    

