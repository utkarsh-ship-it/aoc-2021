import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(s: str) -> int:
    in_vals = s.splitlines()
    counts = [0] * len(in_vals[0])
    for val in in_vals:
        for i, c in enumerate(val):
            if c == '1':
                counts[i] += 1

    gamma = 0
    epsilon = 0

    for i in range(len(in_vals[0])):
        gamma <<= 1
        epsilon <<= 1
        if counts[i] > len(in_vals) // 2:
            gamma += 1
        else:
            epsilon += 1
    
    return gamma * epsilon

with open(INPUT_TXT) as f:
    print(compute(f.read()))