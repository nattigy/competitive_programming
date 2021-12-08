def buggySorting(n):
    return "".join(("2 "*(n - 1) + "1")) if n > 2 else "-1"
    
print(buggySorting(int(input())))