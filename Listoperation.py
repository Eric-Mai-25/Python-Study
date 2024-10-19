def listoperation(list):
    sum = 0 
    largest = 0 
    for i in list:
        sum += i
        if i > largest:
            largest = i
    
    average = 0

    average = sum / len(list)

    print( sum , average, largest)
    return


listoperation([1,2,3,4,5,500])