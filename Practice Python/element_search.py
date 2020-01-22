def list_o(a):
    a.sort()
    finding_num = int(input("Which number are you finding for?"))
    if finding_num in a:
        print("Yes,", finding_num, "is in list", a)
    else:
        print("No,", finding_num, "is not in list", a)
