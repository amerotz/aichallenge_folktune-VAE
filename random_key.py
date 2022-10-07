import json
import os
import numpy as np

np.random.seed(0)

with open('test.abc', 'r') as f:
    data = f.read()

with open('modes_n_keys.json', 'r') as f:
    modes = json.load(f)

transpose = {
    'A':  -3,
    'B': -1,
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7
}

data = data.split('\n')
data = [' '.join(data[n:n+4]) for n in range(0, len(data), 4)]

count = 0
for (i, reel) in enumerate(data):

    try:
        mode = reel.split(' ')[2][3:]

        choices = modes[mode][0]
        probs = modes[mode][1]
        key = np.random.choice(choices, p=probs)

        semitones = transpose[key]

        reel = reel.split(' ')
        name = f'Reel {i}'
        reel = f'{reel[0]}\nT:{name}\nM:4/4\n{reel[2]}\nL:1/8\n{" ".join(reel[3:])}'

        file = f'tmp/{i}.abc'
        with open(file, 'w') as f:
            f.write(reel)

        string = f'abc2abc {file} -t {semitones} -u -e -s'
        os.system(string)
        count += 1
    except:
        continue

    if count == 1000:
        break
