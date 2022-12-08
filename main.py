from fractions import Fraction
import copy

A, B, X0 = [], [], []
D, Din, L, U, Bj, Cj, S = [], [], [], [], [], [], []  # NOQA


def printer_2dimensions(any_list, lenght):  # NOQA
    for LINES in range(n):
        print("∣  ", end="")
        for COLUMNS in range(n):
            try:
                print(
                    f"{str(Fraction(float(any_list[LINES][COLUMNS])).limit_denominator(max_denominator=100000)):{int(lenght)}}",
                    end=' ')
            except (ValueError, TypeError):
                print(f"{str(any_list[LINES][COLUMNS]):{int(lenght)}}", end=' ')
        print("∣")
    print()


def printer_1dimension(any1_list):
    for K in any1_list:
        try:
            print(f"∣  {str(Fraction(K[0]).limit_denominator(max_denominator=100000)):3} ∣")
        except (ValueError, TypeError):
            print(f"∣ {K[0]} ∣")
    print()


n = int(input("number of equations : "))
# making the matrix
for lines in range(n):
    lines_list = []
    B_lines = []
    equations = input(f"Equation {lines + 1} = ")
    for columns in range(n):
        if columns == 0:
            v = float(equations[0: equations.index("x")])
        else:
            v = float(equations[
                      equations.index("xyzabcdefghijklmnopqrstuvw"[columns - 1]) + 1: equations.index(  # NOQA
                          "xyzabcdefghijklmnopqrstuvw"[columns])])  # NOQA

        lines_list.append(v)
    w = equations[equations.index("=") + 1::]
    B_lines.append(float(w))
    B.append(B_lines)
    A.append(lines_list)
print("A : ")
printer_2dimensions(A, 6)
# Making X0
for mat in range(n):
    X0_lines = []  # NOQA
    X0_lines.append(int(input(f"X0 line {mat + 1} : ")))
    X0.append(X0_lines)
order = int(input("Order : "))


# Making lists with 0's
for _ in range(n):
    L_lines = []
    U_lines = []
    D_lines = []
    Din_lines = []

    for _ in range(n):
        L_lines.append(0)
        U_lines.append(0)
        D_lines.append(0)
        Din_lines.append(0)

    L.append(L_lines)
    U.append(U_lines)
    D.append(D_lines)
    Din.append(Din_lines)

# Making D,L,U
for i in range(n):
    for j in range(n):
        if i == j:
            D[i][j] = A[i][j]  # NOQA : 67
            Din[i][j] = 1 / A[i][j]  # NOQA : 77
        else:
            D[i][j] = 0
            Din[i][j] = 0
        if i > j:
            L[i][j] = - A[i][j]  # NOQA : 71
        else:
            L[i][j] = 0
        if i < j:
            U[i][j] = - A[i][j]  # NOQA : 75
        else:
            U[i][j] = 0
print("L:")
printer_2dimensions(L, 6)

print("U:")
printer_2dimensions(U, 6)

print("D:")
printer_2dimensions(D, 6)

print("inverse D:")
printer_2dimensions(Din, 6)


def multiply(m1, m2):
    lin = len(m1)
    col = len(m2[0])

    multiplied = []
    for _ in range(lin):  # making empty matrix
        multiplied_lines = []
        for _ in range(col):
            multiplied_lines.append(0)
        multiplied.append(multiplied_lines)

    for J in range(len(m1)):  # lines of matrix 1 (slow)
        for I in range(len(m2[0])):  # columns of matrix 2 (fast) # NOQA
            for v in range(len(m2)):  # counter # NOQA
                multiplied[J][I] += m1[J][v] * m2[v][I]

    return multiplied


def sum_mat(m1, m2):
    # making empty matrix
    sum_matrix = []
    for p in range(len(m1)):
        s_lines = []
        for u in range(len(m2[0])):
            s_lines.append(0)
        sum_matrix.append(s_lines)

    for ls in range(len(m1)):
        for cs in range(len(m2[0])):
            sum_matrix[ls][cs] = m1[ls][cs] + m2[ls][cs]
    return sum_matrix


Bj = multiply(Din, sum_mat(L, U))
Cj = multiply(Din, B)
print("Bj: ")
printer_2dimensions(Bj, 6)
print("Cj: ")
printer_1dimension(Cj)

# main loop for calculating the answer
Xn = X0
print('\nX0 : ')
printer_1dimension(X0)
for h in range(order):
    S = sum_mat(multiply(Bj, Xn), Cj)
    Xn = copy.deepcopy(S)
    print(f"X({h + 1})")
    printer_1dimension(S)

print("\nSolution : ")
printer_1dimension(S)
