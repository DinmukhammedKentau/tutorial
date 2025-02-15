from datetime import datetime
date1=datetime.now()
date2=datetime.strptime(
    "2025/02/01 20:10:02.233213",
    "%Y/%m/%d %H:%M:%S.%f"
)
total1=date1-date2
print(total1.total_seconds())