from datetime import datetime

now = datetime.now()

date = now.strftime("%d/%m/%Y %H:%M:%S")

print(date)