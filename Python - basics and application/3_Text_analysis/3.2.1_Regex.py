import re
import sys

pattern = r'cat'

for line_ in sys.stdin:
    line = line_.rstrip()
    if match_list := re.findall(pattern, line):
        if len(match_list) >= 2:
            print(line)

