import re
text = "abbbb ak ab erg asd abb asd"
matches=re.findall(r"\bab{2,3}\b",text)
print(matches)
"""ab{2,3} — бұл регулярлы өрнек 'a' әрпінен кейін 
2 немесе 3 'b' болуы керек дегенді білдіреді."""