from datetime import datetime,timedelta
td=datetime.today()
oneday=timedelta(1)
print(f"Yesterday: {td-oneday}")
print(f"Today: {td}")
print(f"Tomorrow: {td+oneday}")