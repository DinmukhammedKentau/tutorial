import re
text="abbbbb a ab erg"
matches=re.findall(r"ab+",text)
print(matches)
"""ab+ деген регулярлы өрнек 
"a" әрпінен кейін бір немесе бірнеше 
"b" әріптері болуы керек дегенді білдіреді."""