import re
str=" aaba a  "
matches=re.findall(r"ab*",str)
print(matches)
