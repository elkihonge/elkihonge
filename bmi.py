#allow user to place input
Weight = input("Enter weight: ")
Height = input("Enter height: ")

#put integers
weight = float(Weight)
height = float(Height)

#calculation
bmi_calc = (weight/height**2)
print(bmi_calc)

#give it a scale
if bmi_calc <= 18.0:
    print("underweight")
elif bmi_calc <= 29.0:
    print("normal weight")
elif bmi_calc <= 34.0:
    print("overweight")
else:
    print("obese")
