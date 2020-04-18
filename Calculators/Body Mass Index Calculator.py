print("[Enter your height]")
Feet = int(input("Feet: "))
Inches = int(input("Inches: ")) + (Feet * 12)
print("[Enter your weight]")
Weight = float(input("Pounds: "))

BMI = int(((703 * Weight) / (Inches**2)))

if BMI < 19:
    print("Your BMI is: " + str(BMI) + " You are underweight, you may need to gain weight.")
else:
    if BMI > 25:
        print("Your BMI is: " + str(BMI) + " You are overweight, you may need to lose weight.")
    else:
        print("Your BMI is: " + str(BMI) + " You have a healthy weight.")
