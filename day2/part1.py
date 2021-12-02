import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(s: str) -> int:
    numbers = [line.split() for line in s.splitlines()]

    horizontal = 0
    depth = 0
    
    for num in numbers:
        if num[0] == "forward":
            horizontal += int(num[1])
        elif num[0] == "down":
            depth += int(num[1])
        elif num[0] == "up":
            depth -= int(num[1])
    
    return horizontal*depth

with open(INPUT_TXT) as f:
    print(compute(f.read()))