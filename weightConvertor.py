# convert from KGS to Pounds(Lbs)
weight = float(input("Enter weight in Kgs: "))
# 1kg = 2.20462
pound = 2.20462
weight_in_lbs = float(pound * weight)
convert_to_2dp = "{:.2f}".format(weight_in_lbs)
print(convert_to_2dp)