name = "drew"
height_m = 1.79
weight_kg = 110

bmi = weight_kg / (height_m ** 2)
print("bmi:  ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")