import re
text="London 55 a5 is the capital don city of Great Britain"
match=re.findall(r"[^0-9][0-9]",text)
print(match)
"""^ osy zhoq degen magyna beredi"""