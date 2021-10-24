import time
import math

def Pitagoras_v0(l):
    triangles = []
    start_time = time.time()
    for a in range (1,l):
        for b in range (1,l):
            for c in range (1,l):
                if a**2 + b**2 == c**2 and a+b+c == l:
                    triangle = (a,b,c)
                    triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return(True, triangles, end_time - start_time)
    else: 
        return(False,end_time - start_time)

def Pitagoras_v1(l):
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    for a in range (1,triangle_condition):
        for b in range (1,triangle_condition):
            for c in range (1,triangle_condition):
                if a**2 + b**2 == c**2 and a+b+c == l:
                    triangle = (a,b,c)
                    triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return(True, triangles, end_time - start_time)
    else: 
        return(False,end_time - start_time)

def Pitagoras_v2(l):
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    for a in range (1,triangle_condition):
        for b in range (a,triangle_condition):
            if a**2 + b**2 == (l-a-b)**2:
                triangle = (a,b,(l-a-b))
                triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return(True, triangles, end_time - start_time)
    else: 
        return(False,end_time - start_time)


def Pitagoras_v3(l):
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    for a in range (1,triangle_condition):
        for b in range (a+1,triangle_condition):
            if math.sqrt(a**2+b**2)%1 == 0:
                if a**2 + b**2 == (l-a-b)**2:
                    triangle = (a,b,(l-a-b))
                    triangles.append(triangle)
    end_time = time.time()
    if len(triangles) != 0:
        return(True, triangles, end_time - start_time)
    else: 
        return(False,end_time - start_time)


def Pitagoras_v4(l):
    counter = 0
    triangles = []
    start_time = time.time()
    triangle_condition = math.ceil(l/2)
    max_of_short = int(l/3)
    for a in range (1,max_of_short):
        for b in range (a+1,triangle_condition):
            if math.sqrt(a**2+b**2)%1 == 0:
                counter += 5
                if a**2 + b**2 == (l-a-b)**2:
                    counter += 7
                    triangle = (a,b,(l-a-b))
                    triangles.append(triangle)
                else:
                    counter += 7
            else:
                counter += 5
    end_time = time.time()
    if len(triangles) != 0:
        return(True, counter, triangles, end_time - start_time)
    else: 
        return(False, counter, end_time - start_time)


if __name__ == "__main__":
    print(Pitagoras_v2(1000))
    print(Pitagoras_v3(1000))
    print(Pitagoras_v4(999))