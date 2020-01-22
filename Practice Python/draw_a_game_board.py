size = int(input("What size of game board do you want to draw?"))
count = 0
while count <= size:
    if count != size:
        print(' ---' * size)
        print('|   ' * (size + 1))
        count += 1
    elif count == size:
        print(' ---' * size)
        break
