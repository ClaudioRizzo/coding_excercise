def add_one(a):
    N = len(a)
    carry = 1
    for i in range(N-1, -1, -1):
        value = a[i]
        if value < 0 or value > 9:
            raise Exception("Malformed array.. aborting")
        _sum = value + carry
        if _sum >= 10:
            if i == 0:
                raise Exception("Overflow")
            a[i] = 0
            carry = 1
        else:
            a[i] = _sum
            carry = 0
            break  # We can finish here

    return a

print(add_one([9,9,9,9,9]))
