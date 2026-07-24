#BMI Calculator
weight = int(input("Enter your weight(kg) : "))
height = float(input("Enter your height(m) : "))
BMI = weight/(height**2)
print(f"Your BMI : {BMI:.2f}")

#BMI Categories
if BMI < 18.5:
    print("Your BMI Categories : Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Your BMI Categories : Normal weight")
elif BMI >= 25.0 and BMI <= 29.9:
    print("Your BMI Categories : Overweight")
elif BMI >= 30:
    print("Your BMI Categories : Obese")
