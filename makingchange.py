c = int(input("number of cents: "))
t = c//200
n = c%200

print ("toonies: " + str(t))
l = n//100
n = n%100

print ("loonies: " + str(l))
q = n//25
n = n%25

print ("quarters: " + str(q))
d = n//10
n = n%10

print ("dimes: " + str(d))
ni = n//5
n = n%5

print ("nickels " + str(ni))
p = n//1

print ("pennies: " + str(p))


