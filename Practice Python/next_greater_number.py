# find next greater number with same set of digits

def next_greater(n):
    answer = None
    n = [int(m) for m in str(n)]
    for i in reversed(range(1,len(n))):
        if n[i-1] < n[i]:
            break
    if (i-1 == 0):
        answer = 'Not Possible'

    elif (i == len(n)-1):
        n[i-1], n[i] = n[i], n[i-1]
        answer = ''.join(map(str,n))

    else:
        after_digits = [int(n[k]) for k in range(i,len(n))]
        smallest = min([gt for gt in after_digits if gt>n[i-1]])
        smallest_idx = after_digits.index(smallest)
        n[i-1], after_digits[smallest_idx] = after_digits[smallest_idx], n[i-1]
        answer = ''.join(map(str, [n[p] for p in range(i)] + sorted(after_digits)))

    return answer
