import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input2.txt')

def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    
    count = 0
    for i, n in enumerate(numbers[3:], start=3):
        if n > numbers[i - 3]:
            count += 1
    return count

with open(INPUT_TXT) as f:
    print(compute(f.read()))