s = int(input("number of seconds: "))

#DAYS
d = s//86400
n = s%86400

#HOURS
h = n//3600
n = n%3600

#MINUTES
m = n//60
n = n%60

#SECONDS
sec = n//1

print(str(d) + ":" + str(h) + ":" + str(m) + ":" + str(sec))