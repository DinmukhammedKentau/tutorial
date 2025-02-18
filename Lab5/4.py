import re
text = "Dima Salem alEm python"
matches=re.findall(r"[A-Z]+[a-z]+",text)
print(matches)