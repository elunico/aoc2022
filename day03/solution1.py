import sys
import os


def alleq(it):
    it = iter(it)
    try:
        first = next(it)
    except StopIteration:
        return True
    return all(i == first for i in it)


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage python3 solution.py INPUT_FILE")

    with open(sys.argv[1]) as f:
        sacks = f.readlines()

    psum = 0
    for sack in sacks:
        sack = sack.strip()
        left, right = set(sack[:len(sack)//2]), set(sack[len(sack)//2:])
        # print(left, right)
        overlaps = [i for i in left if i in right]
        # print(overlaps)
        priorities = [(ord(i.lower()) - ord('a')+1) + (26 if i.lower() != i else 0) for i in overlaps]
        print(priorities)
        psum += sum(priorities)

    os.system('echo "{}" | pbcopy'.format(psum))


if __name__ == '__main__':
    raise SystemExit(main())
