#Extract a substring with regular expressions: re.search(), re.findall()
import re

s = '0049-155-2050-6677'

print(re.search(r'\d+', s))
# <re.Match object; span=(0, 4), match='0049'>
m = re.search(r'\d+', s)
# to get the result
print(m.group())
# 0049

print(type(m.group()))
# <class 'str'>
