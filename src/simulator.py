def split_allele(p1, p2):
    allele_p1 = [char for char in p1]
    allele_p2 = [char for char in p2]

    return allele_p1, allele_p2

def calculate(allele_p1, allele_p2):
    punnett_square = []

    for i in range(0, len(allele_p1)):
        row = []
        for j in range(0, len(allele_p2)):
            row.append(allele_p1[i] + allele_p2[j])
        punnett_square.append(row)

    # Sort punnett square
    for i in range(0, len(punnett_square)):
        for j in range(0, len(punnett_square[i])):
            sorted_chars = sorted(punnett_square[i][j],key=str.islower)

            punnett_square[i][j] = "".join(sorted_chars)

    return punnett_square

def calculate_probabilities(punnett_square):
    total = len(punnett_square) ** 2

    counts = {}

    for row in punnett_square:
        for gene in row:
            if gene in counts:
                counts[gene] += 1
            else:
                counts[gene] = 1
        
    probabilities = {}

    for count in counts:
        probabilities[count] = counts[count] / total

    return probabilities

def print_punnett_cross(punnett_square, row_headers, col_headers):
    rows = len(punnett_square)
    cols = len(punnett_square[0]) if rows else 0

    all_strings = [""]
    all_strings.extend(row_headers)
    all_strings.extend(col_headers)
    for row in punnett_square:
        all_strings.extend(row)

    width = max(len(s) for s in all_strings)

    def border(left, mid, right, fill="─"):
        segment = fill * (width + 2)
        return left + segment + (mid + segment) * cols + right

    def cell_row(cells):
        return "│" + "│".join(f" {c.center(width)} " for c in cells) + "│"

    top = border("┌", "┬", "┐")
    header_div = border("├", "┼", "┤")
    bottom = border("└", "┴", "┘")

    print(top)
    print(cell_row([""] + col_headers))
    print(header_div)
    for i, row in enumerate(punnett_square):
        print(cell_row([row_headers[i]] + row))
        if i < rows - 1:
            print(header_div)
    print(bottom)

def print_probabilities(probabilities):
    print(f"{"Genotype":<10} | {"Probability":<10}")
    print("-" * 43)
    for key, value in probabilities.items():
        percent = str(value * 100) + "%"
        print(f"{str(key):<10} | {percent:<10}")