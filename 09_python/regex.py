import re

patterns = ['term1', 'term2']

text = 'this is a string with term1'

for pattern in patterns:
    print('i am searching for' + pattern)

    if re.search(pattern, text):
        print('match!')
    else:
        print('no match!')

re.search()

re.split()

re.findall()
