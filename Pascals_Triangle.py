def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    triangle = []

    def compute_row(row):
        if row == 0:
            return [1]
        else:
            previous_row = compute_row(row - 1)
            current_row = [1]
            for i in range(len(previous_row) - 1):
                current_row.append(previous_row[i] + previous_row[i + 1])
            current_row.append(1)
            return current_row

    for row in range(row_count):
        triangle.append(compute_row(row))

    return triangle
