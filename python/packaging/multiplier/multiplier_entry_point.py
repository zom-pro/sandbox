"""
This interfaces exposes the entry point to multiplier
"""
import sys
from multiplier.multiplier import multiply_sum


def run():
    # the first argument is the name of the file name
    if len(sys.argv) != 5:
        # you might want to handle non-number gracefully as well.
        raise ValueError("Incorrect number of arguments, you need 4!")


    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])
    e = multiply_sum(a, b, c, d)
    print(e)


if __name__ == "__main__":
    run()