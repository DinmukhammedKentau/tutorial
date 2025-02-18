import re
text = "avada_kedavra bratan bro_SAMTYBRO ok_koooooo"
matches=re.findall(r"[a-z]+_[a-z]+",text)
print(matches)
"""[a-z]+_[a-z]+ — 
бұл регулярлы өрнек кіші әріптерден тұратын бір 
немесе бірнеше сөздерді және олардың арасында үзік сызық (underscore, "_")
 бар екенін тексереді."""
"""[a-z]+_[a-z]+$ егер осыган $ доллар косатын болсак ол тек 
ен сонын гана тексереди"""