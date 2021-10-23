def pitagoras(o):
    o = (int(input("Enter the perimeter of a triangle: ")))
    for a in range(1, o):
        for b in range(1, o):
            for c in range(1, o):
                if a**2 + b**2 == c**2 and a + b + c == o:
                    return a, b, c
    else:
        return "There is no pythagorean triple whose sum is: " + str(o)


print(pitagoras(""))
