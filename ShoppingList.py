
def Shopping(list , default = []):
    print(list)
    command = input("What would you like to do? 'Add' 'Delete' 'View'")

    if command == "Add":
        item = input("What would you like to add?")
        list.append(item)

    if command == "Delete":
        print(list)
        item = input ("What would you like to delete")
        list.remove(item)

    if command == "View":
        print(list)

    if command == "End":
        return
    
    Shopping(list)

    return  

Shopping([])