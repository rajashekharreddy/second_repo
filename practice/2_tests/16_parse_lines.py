import re

for i in range(lines):
    for i in re.finditer(r'.+?(#[A-F0-9]{3,6})',input(),re.I):

    print(i.group(1))