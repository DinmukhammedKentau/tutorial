import re
text="HelloWorld"
match=re.split(r"(?=[A-Z])",text)
print(match)
"""split деген кыркып тастайды"""