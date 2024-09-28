weight=float(input("enter your weight : "))
unit=input("kilograms or pounds? (K or L)")

if unit=="k":
    weight=weight*2.205
    unit="Lbs."
    print(f"your wright is {round(weight,1)} {unit}")

elif unit=="L":
    weight=weight/2.205
    unit="kg."
    print(f"your wright is {round(weight,1)} {unit}")

else:
    print("{unit} is not a valid unit")

