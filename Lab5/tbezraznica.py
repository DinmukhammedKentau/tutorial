import re
text="London is tha capital Don don city of Great Britain"
match=re.findall(r"[dD]on",text)
print(match)
"""[]degen bez raznica degen magyna"""