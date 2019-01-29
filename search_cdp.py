# This program will parse the show_command output and find the
# CDP Neighbor ID from the given command output file.

import glob
import os
import re

os.chdir('/Users/jagadnag/Desktop/projects/asr1k/raw_asr1k')
for file in glob.glob('*cdp_neighbors_detail.txt'):
    print file

    pattern = re.compile(r'Device\sID:\s([a-zA-Z0-9.-]+)')

    with open(file, 'r') as f:
        contents = f.read()

        matches = pattern.finditer(contents)

    for match in matches:
        print(match.group(0))
