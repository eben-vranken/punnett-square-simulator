def calculate(p1, p2):
    allele_p1 = [char for char in p1]
    allele_p2 = [char for char in p2]

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

    print(punnett_square)