def convert(ml):
    tsp = round(float(ml) * .20)
    return tsp
ml = raw_input("amount in millimeters?")
tsp = convert(ml)
print(ml + "millimeters is equal to" + str(tsp) + "teaspoons")
