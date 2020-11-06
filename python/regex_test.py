import re

text = '''

This is my text 

I want to replace Company Name11-03-2020 name name 

to a new line
'''

pattern = re.compile('(?<=Company Name).?')

value = re.sub(pattern, "\n1", text)

print(value)