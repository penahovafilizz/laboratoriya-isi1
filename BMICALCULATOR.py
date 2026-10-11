weight=float(input("Enter your weight in kg: "))
height=float(input("enter your height in meters: "))
bmi=weight/(height**2)
print("your bmi is:" , bmi)
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal")
elif bmi<30:
    print("overweight")
else:
     print("obesity") 