mas = [4, 7, 2, 3, 1, 5, 9, 8]


def find_min(mas):
    min = mas[0]
    for z in mas:
        if z < min:
            min = z
    return min


def arf_min(mas):
    s = 0
    for z in mas:
        s = s + z
    s = s / len(mas)
    return s


print("Mинимума в массиве:", (find_min(mas)))
print("Среднее арифметическое с массиве:", (arf_min(mas)))

