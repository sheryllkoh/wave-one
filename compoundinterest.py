i = int(input("inital balance: "))
first = i * (1 + 0.04)
second = i * (1 + 0.04)**2
third = i * (1 + 0.04)**3

print ("first year: " + "$" + "%.2f" % round(first,2))
print("second year: " + "$" + "%.2f" % round(second,2))
print("third year: " + "$" + "%.2f" % round(third,2))