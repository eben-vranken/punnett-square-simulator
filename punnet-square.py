from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("p1", help="Parental genotypes of parent 1")
    parser.add_argument("p2", help="Parental genotypes of parent 2")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    print(args.p1)
    print(args.p2)