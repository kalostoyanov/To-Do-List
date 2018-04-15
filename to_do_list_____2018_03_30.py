## VARIABLES
todoList = []
newToDo = ""
listIndex = 0
deleteToDoValue = ""
deleteChoice = ""

## DEFINITIONS
# add new to do
def addNewToDo(newtodo):
	if newtodo in todoList:
		print("This value is already added. Please use command 'print' to see your current to do list.")
	else:
		todoList.append(newtodo)
		print("Added.")

# print to do list
def printToDoList():
    if todoList:
        print("These is your current to do list:")
        for listIndex in range(len(todoList)):
            print(listIndex + 1, ":", todoList[listIndex])
    else:
        print("Your list is empty.")


# delete to do
def deleteToDo():
    if todoList:
        printToDoList() # displays the current list for reference
  
        # loop to check if user entered value / input
        deleteToDoChoice = None
        while (deleteToDoChoice != "value") or (deleteToDoChoice != "index"):
            #choice value or index
            deleteToDoChoice = input("Please specify if you want to remove a value or index: ").lower()
    
            # if value
            if deleteToDoChoice == "value":
                deleteToDoValue()
                break
                
            # if index
            if deleteToDoChoice == "index":
                deleteToDoIndex()
                break
    else:
        print("Your list is empty. You can use \"add\" to populate it.")

# delete to do value - subfunction
def deleteToDoValue():
    deleteToDoValue = input("Please enter the item you want to delete: ").title()
    #while (deleteToDoValue not in todoList) or (deleteToDoValue != "Exit"): # the two conditions cannot exist together
    while deleteToDoValue not in todoList:
        deleteToDoValue = input("This value is not in the list: Please enter a new one or type \"Exit\" to abort: ").title()
        if deleteToDoValue == "Exit": # escape mechanism from the while loop
            break
    else: # this is an else clause to the loop
            todoList.remove(deleteToDoValue)
            print("Deleted.")

# delete to do index - subfunction
def deleteToDoIndex():
    deleteToDoIndex = input("Please enter the position of the item you want to delete: ")
    deleteToDoIndexErrorCheck = True
    while deleteToDoIndexErrorCheck == True:
        try: # this is meant to avoid errors, but I think that except continue makes it skip
            deleteToDoIndex = int(deleteToDoIndex)-1
            del todoList[deleteToDoIndex]
            deleteToDoIndexErrorCheck = False
            print("Deleted.")
            break
        except IndexError:
            deleteToDoIndex = input("This item does not exist. Please try again or use \"exit\" to abort: ")
            if deleteToDoIndex.title() == "Exit":
                break
        except ValueError:
            print("Did you type in a number?")
            deleteToDoIndex = input("Please try again or use \"exit\" to abort: ")
            if deleteToDoIndex.title() == "Exit":
                break
                    
                    
print("Please enter your command. Options: add, delete, print, exit.")
command = input("").lower()
while command != exit:
	if command == "add":
		addNewToDo(input("Please enter the item you want to add: ").title())
	elif command == "delete":
		deleteToDo()
	elif command == "print":
		printToDoList()
	elif command == "exit":
		break
	else:
		print("Command unrecognized.")
	command = input("Please enter a new command: ")
