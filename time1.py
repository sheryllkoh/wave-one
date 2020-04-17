day = int(input("number of days: "))
hour = int(input("number of hours: "))
minute = int(input("number of minutes: "))
second = int(input("number of seconds: "))

day1 = day * 86400
hour1 = hour * 3600
minute1 = minute * 60
second1 = second * 1

total = day1 + hour1 + minute1 + second1

print(str(total)+ " seconds")
 
