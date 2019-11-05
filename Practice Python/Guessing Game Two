i = 0
j = 100
m = 50
counter = 1
condition = 0
while condition != 'success':
    print(m)
    condition = input("What will you say?")
    if condition == 'too low':
        i = m+1
        counter += 1
        m = int((i + j) / 2)
    elif condition == 'too high':
        j = m-1
        counter += 1
        m = int((i+j)/2)
    else:
        print('It took ', counter, 'attempts')
