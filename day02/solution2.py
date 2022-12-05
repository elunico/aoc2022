import sys
import os

tools = {
    'A': 0,
    'B': 1,
    'C': 2
}
status = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}


def winner_tool(them):
    return (tools[them] + 1) % 3


def draw_tool(them):
    return tools[them]


def lose_tool(them):
    return ((tools[them] + 3) - 1) % 3


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage python3 solution.py INPUT_FILE")

    with open(sys.argv[1]) as i:
        moves = i.readlines()

    score = 0

    for move in moves:
        them, end = move.strip().split(' ')
        fn = winner_tool if end == 'Z' else (draw_tool if end == 'Y' else lose_tool)
        score += status[end] + (fn(them) + 1)

    print(score)

    os.system('echo "{}" | pbcopy'.format(score))


if __name__ == '__main__':
    raise SystemExit(main())
