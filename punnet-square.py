from argparse import ArgumentParser
from src import simulator

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("p1", help="Parental genotypes of parent 1")
    parser.add_argument("p2", help="Parental genotypes of parent 2")

    # Optional args
    parser.add_argument("-g", "--grid", action="store_true", help="Print the punnett square")
    parser.add_argument("-p", "--probabilities", action="store_true", help="Print the genotype probabilities")

    args = parser.parse_args()

    if not args.grid and not args.probabilities:
        print("Either -g or -p flags are required.\nUse --help for more information")
        exit(1)

    return args

if __name__ == "__main__":
    args = parse_args()

    if any(char.isdigit() for char in args.p1) or any(char.isdigit() for char in args.p2):
        print("Parent genotypes cannot contain numerical characters.")
        exit(1)

    if args.p1.upper() != args.p2.upper():
        print("Parent genotypes are not of the same type.\nInput a monohybrid cross.")
        exit(1)
    
    allele_p1, allele_p2 = simulator.split_allele(args.p1, args.p2)
    punnett_square = simulator.calculate(allele_p1, allele_p2)

    if args.grid:
        simulator.print_punnett_cross(punnett_square, allele_p1, allele_p2)
    
    if args.probabilities:
        probabilities = simulator.calculate_probabilities(punnett_square)
        simulator.print_probabilities(probabilities)