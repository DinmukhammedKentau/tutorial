import re

text="ThisIsAString"
match=re.sub(r"([a-z])([A-Z])",r"\1_\2",text)
print(match)
"""\1 \2 бул типо \1 деген биринши баган 
\2 деген 2 ши баган и сонын арасына пробель кой деп жатырмын"""