def convert_cel_to_far(C):
    F=C*9/5+32
    print(f"{C} degrees F={F:.2f} degrees C")
def convert_far_to_cel(F):
    C=(F-32)*5/9
    print(f"{F} degrees C={C:.2f} degrees F")
a=float(input("Enter a temperature in degrees F:"))
convert_cel_to_far(a)
b=float(input("Enter a temperature in degrees C:"))
convert_far_to_cel(b)