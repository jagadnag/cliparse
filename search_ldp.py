# This program will parse the show_command output and find the
# LDP Neighbor ID from the given command output file.

import glob
import os
import re

os.chdir('/Users/jagadnag/Desktop/projects/asr1k/raw_asr1k')
for file in glob.glob('*mpls_ldp_neighbor.txt'):
    print file

    pattern = re.compile(r'Peer\sLDP\sIdent:\s([a-zA-Z0-9.-]+)')

    with open(file, 'r') as f:
        contents = f.read()

        matches = pattern.finditer(contents)

    for match in matches:
        print(match.group(0))
