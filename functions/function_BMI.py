def calculate_BMI():

 try:
    weight = float(input("Enter Weight: "))
    height = float(input("Enter Height: "))

    calculate_BMI = (weight/height**2)

    print(calculate_BMI)

 except:
    print("Sorry not a number")


calculate_BMI()
