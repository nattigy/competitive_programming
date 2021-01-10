def Division(a, b):
    q = ""
    r = ""
    i = 0
    dd = 0

    while a != "":
        if len(a[: i + 1]) < len(b):
            i += 1
            if i > 1:
                q = q + "0"
            print("1:" + a)
        elif len(a[: i + 1]) == len(b) and a[: i + 1] < b:
            i += 1
            if i > 1:
                q = q + "0"
            print("2:" + a)
        elif len(a[: i + 1]) > len(b):
            q = q + str(int(a[: i + 1]) // int(b))
            r = str(int(a[: i + 1]) % int(b))
            a = a[i + 1 :]
            if a != "" and (r != "0"):
                a = r + a
            i = 0
            print("3:" + a)
        elif len(a[: i + 1]) == len(b) and a[: i + 1] >= b:
            q = q + str(int(a[: i + 1]) // int(b))
            r = str(int(a[: i + 1]) % int(b))
            a = a[i + 1 :]
            if a != "" and (r != "0"):
                a = r + a
            i = 0
            print("4:" + a)

        if len(a) == 0:
            r = r + a if r != "0" else a
            break

        dd += 1

        if dd == 10:
            break

    return (q, r)


print(Division("100", "10"))
