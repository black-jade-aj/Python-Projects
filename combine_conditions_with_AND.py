GPA = float(input("Enter your GPA: "))
lowest_gpa = float(input("Enter the lowest GPA for your program: "))

if GPA >= 3.6 and lowest_gpa >= 3.0:
    print("You are eligible for the scholarship.")
else:
    print("You are not eligible for the scholarship.")
    