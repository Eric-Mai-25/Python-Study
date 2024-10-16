def Phonebook(book):
    command = input("What would you like to do today? Store , View, Search, Exit")

    if command == "Store":
        name = input("Name? ")
        number = input("Number? ")
        book[name] = number

    if command == "View":
        print(book)

    if command == "Search":
        name = input("Who are you looking for?")
        if book[name]:
            print(name + book[name])
        else:
            print("Cannot find that name in the phonebook")

    if command == "Exit":
        return
    Phonebook(book)
    return

Phonebook({})