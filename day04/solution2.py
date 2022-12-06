import sys
import os

from functools import reduce


class Range:
    @classmethod
    def fromstring(cls, string):
        low, high = string.split('-')
        return cls(int(low), int(high))

    def __init__(self, low, high) -> None:
        self.low = low
        self.high = high

    def __eq__(self, __o: object) -> bool:
        if not isinstance(o, Range):
            return NotImplemented
        return __o.left == self.left and __o.right == self.right

    def __contains__(self, other):
        return (self.low <= other.high and self.high >= other.low)


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage python3 solution.py INPUT_FILE")

    with open(sys.argv[1]) as f:
        lines = [i.strip() for i in f.readlines()]

    pairs = [i.split(',') for i in lines]
    pairs = [(Range.fromstring(i[0]), Range.fromstring(i[1])) for i in pairs]
    result = reduce(lambda acc, pair: (acc + 1)if pair[0] in pair[1] or pair[1] in pair[0] else acc, pairs, 0)

    print(pairs)

    print(result)
    os.system('echo "{}" | pbcopy'.format(result))


if __name__ == '__main__':
    raise SystemExit(main())
