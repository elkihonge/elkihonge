#allow user to place input
Weight = input("Enter weight")
Height = input("Entere height")

#put integers
weight = int(Weight)
height = int(Height)

#calculation
bmi_calc = (weight/height**2)
print(bmi_calc)