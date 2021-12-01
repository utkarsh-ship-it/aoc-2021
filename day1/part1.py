import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input1.txt')

def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    prev = numbers[0]
    count = 0
    for n in numbers[1:]:
        if n > prev:
            count += 1
        prev = n
    return count

with open(INPUT_TXT) as f:
    print(compute(f.read()))