def checkPali():
    string = input("What is the string?")
    x = 0
    y = len(string) - 1
    pali = True

    while x != y and x < y:
        if string[x].lower() != string[y].lower():
            pali = False
        x += 1
        y -= 1
    
    print(pali)
    return 

checkPali()