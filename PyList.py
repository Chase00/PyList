import os

def menu(list):
    t = 1
    while (t == 1):

        thisList = list

        print("1. Add an item")
        print("2. Remove an item")
        print("3. List all items")
        print("4. Sort the list")

        print("")

        userChoice = input("What would you like to do?: ")

        if userChoice == "1":
            addItems(thisList)
            menu(thisList)
        if userChoice == "2":
            removeItems(thisList)
            menu(thisList)
        if userChoice == "3":
            listItems(thisList)
            menu(thisList)
        if userChoice == "4":
            sort(thisList)
            menu(thisList)
        if userChoice == "5":
            nameList(thisList)
            menu(thisList)

def listItems(thisList):

    clear = lambda: os.system('cls')
    clear()

    print("Here's your current list: ")

    print("")

    for x in thisList:
        print(x)

    print("")

    cont = input("Press enter to continue...")

    clear = lambda: os.system('cls')
    clear()

def addItems(thisList):

    clear = lambda: os.system('cls')
    clear()

    add = input('Enter something to add: ')
    thisList.append(add)

    print("")
    print("Successfully added: ", add)
    cont = input("Press enter to continue...")

    clear = lambda: os.system('cls')
    clear()

def removeItems(thisList):

    clear = lambda: os.system('cls')
    clear()

    for x in thisList:
        print(x)

    print("")

    delChoice = input('Enter an item to delete: ')

    clear = lambda: os.system('cls')
    clear()

    try:
        thisList.remove(delChoice)

        print(delChoice ,"has been removed.")

        print("")
        print("Revised List:")
        for x in thisList:
            print(x)

        print("")

        cont = input("Press enter to continue...")

    except ValueError:
        print("No item was found: ", delChoice)

        cont = input("Press enter to continue...")

    clear = lambda: os.system('cls')
    clear()

def sort(thisList):

    clear = lambda: os.system('cls')
    clear()

    thisList.sort()

    print("Your list has been sorted from A-Z")
    print("")

    for x in thisList:
        print(x)

    print("")
    cont = input("Press enter to continue...")

    clear = lambda: os.system('cls')
    clear()

def nameList(thisList):

    name = input("feature not done :)")

def main():

    userList = []
    menu(userList)

main()
