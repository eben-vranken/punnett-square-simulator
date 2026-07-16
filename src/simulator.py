def calculate(p1, p2):
    allele_p1 = p1[:len(p1)//2 + len(p1)%2], p1[len(p1)//2 + len(p1)%2:]

    allele_p2 = p2[:len(p2)//2 + len(p2)%2], p2[len(p2)//2 + len(p2)%2:]

    print(allele_p1)
    print(allele_p2)