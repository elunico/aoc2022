import sys


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage python3 solution.py INPUT_FILE")

    with open(sys.argv[1]) as f:
        text = f.read()
        elves = text.split('\n\n')

    highest = -1

    for elf_set in elves:
        cals = sum(int(i) for i in elf_set.split('\n') if i)
        if cals > highest:
            highest = cals

    print(highest)


if __name__ == '__main__':
    raise SystemExit(main())
