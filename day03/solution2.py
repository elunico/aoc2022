import sys
import os


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage python3 solution.py INPUT_FILE")

    psum = 0
    sacks = []
    with open(sys.argv[1]) as f:
        lines = [i.strip() for i in f.readlines()]
        for i in range(0, len(lines), 3):
            b1 = set(lines[i])
            b2 = set(lines[i+1])
            b3 = set(lines[i+2])
            cross = b1 & b2 & b3
            psum += sum([(ord(k.lower()) - ord('a')+1) + (26 if k.lower() != k else 0) for k in cross])

    print(psum)
    os.system('echo "{}" | pbcopy'.format(psum))


if __name__ == '__main__':
    raise SystemExit(main())
