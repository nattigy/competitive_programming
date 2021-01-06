def Division(a, b):
    q = ""
    r = 0
    i = 0
    while a != "" or i != len(a):
        print(a[: i + 1])
        if len(b) > len(a[: i + 1]):

            if len(b) == len(a[: i + 1]) and b < a[: i + 1]:

                q = q + str(int(a[: i + 1]) // int(b))
                r = (int(a[: i + 1]) / int(b)) % 10
                if r != 0:
                    a = str(r) + a[i + 1 :]
                else:
                    a = a[i + 1]
                i = 0
            else:
                i += 1
        else:
            i += 1
    return q


print(Division("544", "53"))
