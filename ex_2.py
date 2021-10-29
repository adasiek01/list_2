import time


def pitagoras(x):
    t_list = []
    x = (int(input("Enter the perimeter of a triangle: ")))
    start = time.time()
    for a in range(1, x):
        for b in range(1, x):
            for c in range(1, x):
                if a**2 + b**2 == c**2 and a + b + c == x:
                    result = (a, b, c)
                    t_list.append(result)
    end = time.time()
    if len(t_list) != 0:
        return True, t_list[0], end - start
    else:
        return "There is no pythagorean triple whose sum is: " + str(x)

def pitagoras_2(x):
    x = (int(input("Enter the perimeter of a triangle: ")))
    for a in range(1, x):
        for b in range(1, x):
            for c in range(1, int(x/2)):
                """
                a + b > c
                so 'c' can not be bigger than half the circumference
                """
                if a**2 + b**2 == c**2 and a + b + c == x:
                    return a, b, c
    else:
        return "There is no pythagorean triple whose sum is: " + str(x)


def pitagoras_3(x):
    x = (int(input("Enter the perimeter of a triangle: ")))
    for a in range(1, x):
        for b in range(1, x):
            c = x - a - b
            if a**2 + b**2 == c**2 and a + b + c == x:
                return a, b, c
    else:
        return "There is no pythagorean triple whose sum is: " + str(x)


def pitagoras_4(x):
    x = (int(input("Enter the perimeter of a triangle: ")))
    """
    a + b + c = x
    a**2 + b**2 = c**2
    operations on patterns
    b = (x - c + (a-b))/2
    a = x - c -b
    """


if __name__ == "__main__":
    print(pitagoras(""))
