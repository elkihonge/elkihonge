#allow user to place input
Weight = input("Enter weight")
Height = input("Enter height")

#put integers
weight = float(Weight)
height = float(Height)

#calculation
bmi_calc = (weight/height**2)
print(bmi_calc)

#give it a scale
if bmi_calc <= 18.0:
    print("You are underweight")
elif bmi_calc <= 29.0:
    print("You are normal weight")
elif bmi_calc <= 34.0:
    print("You are overweight")
else:
    print("You are obese")
