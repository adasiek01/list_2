import time
import math


def pitagoras_v0(l):
    """
    Function that finds pythagorean triples
    :param l: perimeter of a triangle
    :return: pythagorean triple, time of work, number of operations
    """
    counter = 0
    triangles = []
    start_time = time.time()
    for a in range(1, l):
        for b in range(1, l):
            for c in range(1, l):
                counter += 9
                if a**2 + b**2 == c**2 and a+b+c == l:
                    triangle = (a, b, c)
                    triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return True, triangles, end_time - start_time, counter
    else: 
        return False, end_time - start_time, counter


def pitagoras_v1(l):
    """
    Function that finds pythagorean triples
    :param l: perimeter of a triangle
    :return: pythagorean triple, time of work, number of operations
    """
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    counter = 1
    for a in range(1, triangle_condition):
        for b in range(1, triangle_condition):
            for c in range(1, triangle_condition):
                counter += 9
                if a**2 + b**2 == c**2 and a+b+c == l:
                    triangle = (a, b, c)
                    triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return True, triangles, end_time - start_time, counter
    else: 
        return False, end_time - start_time, counter


def pitagoras_v2(l):
    """
    Function that finds pythagorean triples
    :param l: perimeter of a triangle
    :return: pythagorean triple, time of work, number of operations
    """
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    counter = 1
    for a in range(1, triangle_condition):
        for b in range(a, triangle_condition):
            counter += 7
            if a**2 + b**2 == (l-a-b)**2:
                counter += 2
                triangle = (a, b, (l-a-b))
                triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return True, triangles, end_time - start_time, counter
    else: 
        return False, end_time - start_time, counter


def pitagoras_v3(l):
    """
    Function that finds pythagorean triples
    :param l: perimeter of a triangle
    :return: pythagorean triple, time of work, number of operations
    """
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    counter = 1
    for a in range(1, triangle_condition):
        for b in range(a+1, triangle_condition):
            counter += 7
            if math.sqrt(a**2+b**2) % 1 == 0:
                counter += 7
                if a**2 + b**2 == (l-a-b)**2:
                    counter += 2
                    triangle = (a, b, (l-a-b))
                    triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return True, triangles, end_time - start_time, counter
    else: 
        return False, end_time - start_time, counter


def pitagoras_v4(l):
    """
    Function that finds pythagorean triples
    :param l: perimeter of a triangle
    :return: pythagorean triple, time of work, number of operations
    """
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    max_of_short = int(l/3)
    counter = 2
    for a in range(1, max_of_short):
        
        for b in range(a+1, triangle_condition):

            """
            a+1 -> 1
            (a**2+b**2) % 1 -> 4
            if ... == 0: -> 1
            a**2 + b**2 -> 3
            (l-a-b)**2 -> 3
            if ... == ... -> 1
            triangle = .... l-a-b -> 2
            """
            counter += 6
            
            if math.sqrt(a**2+b**2) % 1 == 0:
                counter += 7
                if a**2 + b**2 == (l-a-b)**2:
                    counter += 2
                    triangle = (a, b, (l-a-b))
                    triangles.append(triangle)
        
    end_time = time.time()
    if len(triangles) != 0:
        return True, triangles, end_time - start_time, counter
    else: 
        return False, end_time - start_time, counter


def pitagoras_v4_sh(l):
    """
    Function that finds pythagorean triples
    :param l: perimeter of a triangle
    :return: pythagorean triple, time of work, number of operations
    """
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    max_of_short = int(l/3)
    counter = 2
    for a in range(1, max_of_short):
        for b in range(a+1, triangle_condition):
            square_sum = a**2+b**2
            counter += 6
            if math.sqrt(square_sum) % 1 == 0:
                counter += 4
                if square_sum == (l-a-b)**2:
                    counter += 2
                    triangle = (a, b, (l-a-b))
                    triangles.append(triangle)
                     
    end_time = time.time()
    if len(triangles) != 0:
        return True, triangles, end_time - start_time, counter
    else: 
        return False, end_time - start_time, counter


def pitagoras_v5(l):
    """
    Function that finds pythagorean triples
    :param l: perimeter of a triangle
    :return: pythagorean triple, time of work, number of operations
    """
    triangles = []
    start_time = time.time()
    min_c = int(l/3)+1
    max_c = math.ceil(l/2)
    counter = 3
    for c in range(min_c, max_c):
        a_b_square = c**2 - l**2 + 2*l*c
        counter += 7
        if a_b_square > 0:
            counter += 2
            a_b = math.sqrt(a_b_square)
            if int(a_b) == float(a_b):
                counter += 5
                b = int((l - c + a_b)/2)
                a = int(l - c - b)
                triangle = (a, b, c)
                triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return True, triangles, end_time - start_time, counter
    else: 
        return False, end_time - start_time, counter


def pitagoras_v5_short(l):
    """
    Function that finds pythagorean triples
    :param l: perimeter of a triangle
    :return: pythagorean triple, time of work, number of operations
    """
    start_time = time.time()
    check = 1
    min_c = int(l/3)+1
    max_c = math.ceil(l/2)
    counter = 3
    for c in range(min_c, max_c):
        a_b_square = c**2 - l**2 + 2*l*c
        counter += 7
        if a_b_square > 0:
            a_b = math.sqrt(a_b_square)
            counter += 2
            if int(a_b) == float(a_b):
                b = int((l - c + a_b)/2)
                a = int(l - c - b)
                check = 1
                counter += 5
                end_time = time.time()
                return True, (a, b, c), end_time - start_time, counter
            else:
                check = 0
    end_time = time.time()
    if check == 0:
        return False, end_time - start_time, counter
    

if __name__ == "__main__":
    """
    print(pitagoras_v0(176))
    print(pitagoras_v1(176))
    print(pitagoras_v2(176))
    print(pitagoras_v3(176))
    print(pitagoras_v4(176))
    print(pitagoras_v4_sh(176))
    print(pitagoras_v5(176))
    print(pitagoras_v5_short(176))
    """
