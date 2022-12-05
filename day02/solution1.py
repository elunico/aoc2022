import sys
import os

tools = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def leftwin(me, them):
    return (me == 1 and them == 3) or (me == 2 and them == 1) or (me == 3 and them == 2)


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage python3 solution.py INPUT_FILE")

    with open(sys.argv[1]) as i:
        moves = i.readlines()

    score = 0

    for move in moves:
        them, me = move.strip().split(' ')
        me = tools[me]
        them = tools[them]
        if leftwin(me, them):
            score += me + 6
        elif me == them:
            score += me + 3
        else:
            score += me

    print(score)

    os.system('echo "{}" | pbcopy'.format(score))


if __name__ == '__main__':
    raise SystemExit(main())
