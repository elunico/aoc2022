import sys
import os


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage python3 solution.py INPUT_FILE")

    with open(sys.argv[1]) as f:
        lines = [i.strip() for i in f.readlines()]

    print(result)
    os.system('echo "{}" | pbcopy'.format(result))


if __name__ == '__main__':
    raise SystemExit(main())
