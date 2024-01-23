def items(matrix, values, weights, m, n):
    result = []
    while m > 0 and n > 0:
        if matrix[m][n] == matrix[m][n - 1]:
            while matrix[m][n] == matrix[m][n - 1]:
                n -= 1
        elif matrix[m][n] == matrix[m - 1][n]:
            while matrix[m][n] == matrix[m - 1][n]:
                m -= 1
        result.append((m, values[m]))
        n -= weights[m]
        m -= 1
    return result

def knapsack(values, weights, m, c):
    matrix = [[0] * c for _ in range(m)]

    for i in range(1, m):
        matrix[i][0] = 0

    for j in range(1, c):
        matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, c):
            if j - weights[i] >= 0:
                matrix[i][j] = max(matrix[i - 1][j], values[i] + matrix[i - 1][j - weights[i]])
            else:
                matrix[i][j] = matrix[i - 1][j]

    print("\n\tKnapsack Matrix")
    print(" ", end="")
    for i in range(c):
        print(f"\t{i}", end="")
    print()
    for i in range(m):
        print(i, end="")
        for j in range(c):
            print(f"\t{matrix[i][j]}", end="")
        print()

    print(f"\nMaximum Knapsack Value={matrix[m - 1][c - 1]}\n")

    chosen_items = items(matrix, values, weights, m - 1, c - 1)
    print("\tChoosen Item and Value")
    for item in reversed(chosen_items):
        print(f"{item[0]}\t{item[1]}")

if __name__ == "__main__":
    m = int(input("Enter number of items: ")) + 1
    values = [0] * m
    weights = [0] * m

    for i in range(1, m):
        weights[i] = int(input(f"Enter weight of item {i}: "))
        values[i] = int(input(f"Enter value of item {i}: "))

    print("\nItem\tWeight\tValue")
    for i in range(1, m):
        print(f"{i}\t{weights[i]}\t{values[i]}")

    capacity = int(input("Enter capacity: "))
    knapsack(values, weights, m, capacity + 1)
