import glob
import os
import re

os.chdir('/Users/jagadnag/Desktop/projects/parser/mpls')
for file in glob.glob('*mpls*.txt'):
    print file

    pattern = re.compile(r'Peer\sLDP\sIdentifier:\s\d+.\d+.\d+.\d+')

    with open(file, 'r') as f:
        contents = f.read()

        matches = pattern.finditer(contents)

    for match in matches:
        print(match.group(0))
