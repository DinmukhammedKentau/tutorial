import re
text="iAmYourKing"
match=re.sub(r"([a-z])([A-Z])",r"\1_\2",text)
print(match.lower())
