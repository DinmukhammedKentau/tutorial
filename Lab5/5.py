import re
def get(text):
    matches=re.findall(r"a.*?b$",text)
    if len(matches)>0:
        print(matches)
    else :
        print("No matches")
get("ssajfas'kb")
get("assadab")
get("dslm;v")
get("adlsvb")
"""a.*?b$ — Бұл өрнек 'a' әрпінен басталып, 
ең жақын кездесетін 'b' әрпімен аяқталатын ең қысқа
 (lazy) сәйкестікті табады.
 a.*?b$:

a → 'a' әрпінен басталады.
.*? → Кез келген символдардың ең қысқа мүмкін сәйкестігін іздейді (lazy match).
b$ → 'b' әрпімен жолдың соңында аяқталуы керек ($ – соңын білдіреді)"""