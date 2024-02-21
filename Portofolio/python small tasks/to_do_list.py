#to do list
objectives_list=[]

def meniu():
    print("***********************")
    print("1: Show my list\n"
          "2: Add\n"
          "3: Delete\n"
          "4: Exit\n")

def show_my_list():  
    for index,objective in enumerate(objectives_list):
         print(f"{index + 1}: {objective}")
         print("")

def add():
    add_objective=input("Add your objective: ")
    objectives_list.append(add_objective)
    print("")
    print(f"{add_objective} was added!")

def delete():
    delete_item=input("You shure want to delete? y/n : ")  
    print(f"First objective {objectives_list} was deleted deleted!") 
    if delete_item=="y":
        del objectives_list[0]           
    else:
        print("Return to meniu")


print("*****To Do List*****")

while True:
    meniu()
    print("**********************")

    option=input("Your option?: ")
    print("")

    if option=="1":
        print("YOUR TO DO LIST:")
        print("")
        show_my_list()

    elif option=="2":
        add()

    elif option=="3":
        delete()

    elif option=="4":
        print("Good Bye!")
        break
    
    else:
        print("Incorect")

               