import re
import os

raw = open('c:\\Users/hp/Desktop/Hello.txt' , 'r')
content = raw.read()

match = re.search(r'\b(the church)\b', content)
if match:
    print('True')
else:
    print('False')
