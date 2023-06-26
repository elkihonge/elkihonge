#allow user to place input
Weight = input("Enter weight")
Height = input("Entere height")

#put integers
weight = float(Weight)
height = float(Height)

#calculation
bmi_calc = (weight/height**2)
print(bmi_calc)