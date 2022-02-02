import math
from sys import stdout

LOG_10 = 2.302585092994
# file = open("matrix.txt", "w")
file = open("matrix.txt", "w")
def result_matrix(N):
    if N % 4 == 2:
        display(build_sems(N))
    elif N % 2 == 1:
        ifNotEven(N)
    else:
        DoublyEven(N)
    file.close()

def build_oms(z):
    if z % 2 == 0:
        z += 1
    q = [[0 for j in range(z)] for i in range(z)]
    p = 1
    i = z // 2
    j = 0
    while p <= (z ** 2):
        q[i][j] = p
        ti = i + 1
        if ti >= z:
            ti = 0
        tj = j - 1
        if tj < 0:
            tj = z - 1
        if q[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1

    return q, z

def build_sems(n):
    while n % 4 == 0:
        n += 2
    q = [[0 for j in range(n)] for i in range(n)]
    z = n // 2
    b = z **2
    c = 2 * b
    d = 3 * b
    o = build_oms(z)

    for j in range(0, z):
        for i in range(0, z):
            a = o[0][i][j]
            q[i][j] = a
            q[i + z][j + z] = a + b
            q[i + z][j] = a + c
            q[i][j + z] = a + d

    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, n):
            if i < lc or i > n - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = q[i][j]
                    q[i][j] = q[i][j + z]
                    q[i][j + z] = t

    return q, n


def format_sqr(s, l):
    for i in range(0, l - len(s)):
        pass
    return s + " "


def display(q):
    file = open("matrix.txt", "w")
    # A = [[0] * N for i in range(N)]
    s = q[1]
    k = 1 + math.floor(math.log(s * s) / LOG_10)
    for j in range(0, s):
        for i in range(0, s):
            file.write(format_sqr("{0}".format(q[0][i][j]), k))
            # stdout.write(format_sqr("{0}".format(q[0][i][j]), k))
            # A[j, i] = format_sqr("{0}".format(q[0][i][j]), k)
        file.write('\n')
    # file.close()
    # print(A)

def ifNotEven(N):
    file = open("matrix.txt", "w")
    square = [[0] * N for i in range(N)]
    n = 1
    i, j = 0, N // 2

    while n <= N ** 2:
        square[i][j] = n
        n += 1
        newi, newj = (i - 1) % N, (j + 1) % N
        if square[newi][newj]:
            i += 1
        else:
            i, j = newi, newj

    for line in square:
        for i in line:
            file.write(str(i) + ' ')
        file.write('\n')
    # file.close()

def DoublyEven(n):
    file = open("matrix.txt", "w")
    arr = [[(n * y) + x + 1 for x in range(n)] for y in range(n)]
    for i in range(0, n // 4):
        for j in range(0, n // 4):
            arr[i][j] = (n * n + 1) - arr[i][j]

    for i in range(0, n // 4):
        for j in range(3 * (n // 4), n):
            arr[i][j] = (n * n + 1) - arr[i][j]

    for i in range(3 * (n // 4), n):
        for j in range(0, n // 4):
            arr[i][j] = (n * n + 1) - arr[i][j]

    for i in range(3 * (n // 4), n):
        for j in range(3 * (n // 4), n):
            arr[i][j] = (n * n + 1) - arr[i][j]

    for i in range(n // 4, 3 * (n // 4)):
        for j in range(n // 4, 3 * (n // 4)):
            arr[i][j] = (n * n + 1) - arr[i][j]


    for line in arr:
        for i in line:
            file.write(str(i) + ' ')
        file.write('\n')
    # file.close()


# from main_prog import
#ОСНОВНАЯ ЧАСТЬ
# N = int(input('Введите размерность магического квадрата: '))
# result_matrix(N)
# print('Сумма магического квадрата: ', )
