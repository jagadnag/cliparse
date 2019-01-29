import glob
import os
import re

os.chdir('/Users/jagadnag/Desktop/projects/parser/Inventory')
# os.chdir('/Users/jagadnag/Desktop/Parser')
for file in glob.glob('*inventory*.txt'):
    print file

#    pattern = re.compile(r'\d+.\d+.254.\d?\d?\d?')
    pattern = re.compile(r'PID?.\s[a-zA-Z0-9-.]+')

    with open(file, 'r') as f:
        contents = f.read()

        matches = pattern.finditer(contents)

    for match in matches:
        print(match.group(0))
