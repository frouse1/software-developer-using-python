import argparse
import math
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--square", help="display a square of a given number", type=int)
    parser.add_argument("root", help="display a square root of a given number", type=int)
    # parser.add_argument("-v", "--verbose", action="store_true",
    #                 help="increase output verbosity")
    args = parser.parse_args()
    t_square =args.square**2
    print(f'square is {t_square}')
    #print(f'square is {args.square**2}')
    print(f'root is {math.sqrt(args.root)}')
    # print("hello from argparse!")
    # if args.verbose:
    #     print("verbosity turned on")
    print("Hello from argparse!")

if __name__ == "__main__":
    main()