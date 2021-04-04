def Triangle(num):
    for i in range(1, num + 1):
        print(" " * (num - i), end="")
        print("*" * (i + i - 1))


Triangle(5)