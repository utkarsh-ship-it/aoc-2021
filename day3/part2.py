import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
 
def compute(s: str) -> int:

    in_vals = s.splitlines()

    root = {'cnt': 0}
    for val in in_vals:
        curr = root
        for c in val:
            
            curr['cnt'] += 1
            curr.setdefault(c, {'cnt': 0})
            curr = curr[c]

        curr['cnt'] += 1

    path = []
    curr = root
    while True:
        if curr.get('1', {}).get('cnt', 0) >= curr.get('0', {}).get('cnt', 0):
            curr = curr['1']
            path.append('1')
        else:
            curr = curr['0']
            path.append('0')

        if curr['cnt'] == 1:
            prefx = ''.join(path)
            break
    # import pdb; pdb.set_trace()
    # breakpoint        
    path = []
    curr = root
    while True:
        if curr.get('1', {}).get('cnt', 0) < curr.get('0', {}).get('cnt', 0):
            curr = curr['1']
            path.append('1')
        else:
            curr = curr['0']
            path.append('0')
        
        if curr['cnt'] == 1:
            prefx2 = ''.join(path)
            break
    # import pdb; pdb.set_trace()
    # breakpoint 
    best, = [val for val in in_vals if val.startswith(prefx)]
    worst, = [val for val in in_vals if val.startswith(prefx2)]    
    
    return int(best, 2) * int(worst,2)

with open(INPUT_TXT) as f:
    print(compute(f.read()))