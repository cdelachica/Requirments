def byeduplicate ():
    num = input ("ENTER NUMBERS:")
    num = list (num)
    list = []

    for i in num:
        if i not in list:
            list.append(i)

    print (list)
    byeduplicate()