length = int(input("length of the field in feet: "))
width = int(input("width of the field in feet: "))
acre = 43560
area = ((length * width)/acre)

print(str(area) + " acres")