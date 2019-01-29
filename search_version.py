import glob
import os
import re


os.chdir('/Users/jagadnag/Desktop/projects/parser/CLI')
for file in glob.glob('*version*.txt'):
    # print file
    # Match hostname
    pattern = re.compile(r'([C|c]sr[a-zA-Z]*\d\d\s)')
    with open(file, 'r') as f:
        contents = f.read()
        matches = pattern.findall(contents)

    for hname in matches:
        hostname = hname

    # Match IOS flavor
    pattern = re.compile(r'(Cisco IOS XR)')
    with open(file, 'r') as f:
        contents = f.read()
        matches = pattern.findall(contents)
    for iosname in matches:
        os = iosname

    # Match Version number
    pattern = re.compile(r'(Version \d.\d.\d)')

    with open(file, 'r') as f:
        contents = f.read()
        matches = pattern.findall(contents)
    for version in matches:
        Software = version

    print hostname, os, Software
