import re
text="erkjv, dkgj,. vks.kjvnjf"
match=re.sub(r"[,. ]",":",text )
print(match)
"""r"[,. ]",":" осы кодта озгертеди : осыган """