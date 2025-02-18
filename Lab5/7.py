import re
text="this_is_snake_case"
matches=re.sub(r"_([a-z])",lambda l:l.group(1).upper(),text)
print(matches)
"""([a-z]) osy a men z tin arasy degen soz"""
"""lambda сөзін аударғанда, ол "қысқаша функция"""