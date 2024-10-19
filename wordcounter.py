def wordCount(string):
    words = list(string)
    diction = {}
    for i in words:
        if not diction.get(i):
            diction[i] = 1
        else:
            diction[i] += 1
    
    print(diction)
    return

wordCount('evveeennntttteeeepppp')