import sys
from heapq import *


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage python3 solution.py INPUT_FILE")

    with open(sys.argv[1]) as f:
        text = f.read()
        elves = text.split('\n\n')

    totals = []

    for elf_set in elves:
        cals = sum(int(i) for i in elf_set.split('\n') if i)
        if len(totals) == 3:
            heappushpop(totals, cals)
        else:
            heappush(totals, cals)

    print(sum(totals))


if __name__ == '__main__':
    raise SystemExit(main())
