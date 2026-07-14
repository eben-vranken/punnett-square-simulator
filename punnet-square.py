from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("p1", help="Parental genotypes of parent 1")
    parser.add_argument("p2", help="Parental genotypes of parent 2")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    if args.p1.upper() != args.p2.upper():
        print("Parent genotypes are not of the same type.\nInput a monohybrid cross.")
        exit(1)
    