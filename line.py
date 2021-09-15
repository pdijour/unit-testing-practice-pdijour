# line.py

def find_m(point1, point2):
    m = (point2[1]-point1[1])/(point2[0]-point1[0])
    return m

def find_b(point1, m):
    b = -m * point1[0] + point1[1]
    return b

def find_y(m, x, b):
    y = m * x + b
    return y

def calculate():
    point1 = (1, 1)
    point2 = (2, 2)
    x = 3
    m = find_m(point1, point2)
    b = find_b(point1, m)
    y = find_y(m, x, b)
    print(y)

if __name__ == '__main__':
    calculate()