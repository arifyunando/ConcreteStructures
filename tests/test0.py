cond = True
while cond:
    x = int(input("Input X Value :"))
    y = 10 if (x > 10) else 5 if (x < 5) else x
    print("{} is the Y value".format(y))
    cond = True if input("continue? y/n :") == "y" else False

