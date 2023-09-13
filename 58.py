import re
s="   fly me   to   the moon  "
s = re.sub(' +', ' ', s)
list1 = s.split(' ')
print(len(list1[-1]))