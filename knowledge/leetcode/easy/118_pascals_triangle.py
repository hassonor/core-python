from typing import List


def generate(num_rows: int) -> List[List[int]]:
    triangle = list()

    for row_num in range(num_rows):
        row = [1] * (num_rows + 1)

        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j] + triangle[row_num - 1][j - 1]

        triangle.append(row)

    return triangle


print(generate(5))
