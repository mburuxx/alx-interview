#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            # Generate elements in between first and last elements of each row
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    return triangle
