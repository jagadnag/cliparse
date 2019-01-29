import glob
import os
import re

os.chdir('/Users/jagadnag/Desktop/projects/asr1k/raw_asr1k')
for file in glob.glob('*show_ip_ospf_neighbor.txt'):
    print file

    pattern = re.compile(r'\d+.\d+.254.\d?\d?\d?')

    with open(file, 'r') as f:
        contents = f.read()

        matches = pattern.finditer(contents)

    for match in matches:
        print(match.group(0))
