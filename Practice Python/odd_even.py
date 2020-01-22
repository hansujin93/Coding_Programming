check = int(input("check?"))
num = int(input("divide by what number?"))
if check % 4 == 0:
    print(check, "is a multiple of 4")
elif check % 2 == 0:
    print(check, "is even")
else:
    print(check, "is odd")
    
if check % num == 0:
    print(check, "is dividable by", num)
else:
    print(check, "is not dividable by", num)
