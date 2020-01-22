def rm_duplicates(a):
    new = []
    for i in range(len(a)):
        if a[i] not in a[:i]:
            new.append(a[i])
        else:
            pass
    return new
