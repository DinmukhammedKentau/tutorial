import re

text = "London is the capital don city of Great Britain"
match = re.findall(r"\bdon\b", text)
print(match)
"""If i want to find only 'don' then i need to write 
r"\b     \b" """
