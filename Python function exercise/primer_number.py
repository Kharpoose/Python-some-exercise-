def primer_number(x):
    if (x == 1):
        return False
    elif (x == 2):
        return True
    else:
        for z in range(2, x):
            if (x % z == 0):
                return False
        return True

print(primer_number(5))
