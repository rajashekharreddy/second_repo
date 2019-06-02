"""
A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.

"""

import re
for i in range(int(input())):

    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u), "test1"
        assert re.search(r'\d\d\d', u), "test2"
        assert not re.search(r'[^a-zA-Z0-9]', u), "test3"
        assert not re.search(r'(.)\1', u), "test4"
        assert len(u) == 10, "test5"
    except Exception as e:
        print('Invalid')
    else:
        print('Valid')
