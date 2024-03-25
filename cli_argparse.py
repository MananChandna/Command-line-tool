import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("integer", type=int, nargs="+")
    parser.add_argument("--sum", dest='accumulate', action='store_const', const=sum, default=max)
    args = parser.parse_args()
    print(args.accumulate(args.integer))
