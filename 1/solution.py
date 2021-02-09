import sys

def part1(entries):
    # Input only has 200 values, O(n^2) is fine
    for entry1 in entries:
        for entry2 in entries:
            if entry1 + entry2 == 2020:
                return entry1 * entry2


def part2(entries):
    # O(n^3) is still fast enough
    for entry1 in entries:
        for entry2 in entries:
            for entry3 in entries:
                if entry1 + entry2 + entry3 == 2020:
                    return entry1 * entry2 * entry3


if __name__ == '__main__':
    # Read Input
    entries = []
    for line in sys.stdin:
        entries.append(int(line))

    print(part1(entries))
    print(part2(entries))