temprature=float(input("enter temprature measured"))
unit=input("enter K for kelvin, F of fahrenhiet and C for °Celcius: (K,F or C)")

if unit=="K":
    te1=temprature+273    #conv in celcius.      
    t1=round(te1,1)
    te2=1.8*(temprature-273)+32 #conv in fahrenhiet.
    t2=round(te2,1)
    u1="°C"
    u2="°F"
    print(f"given tempature is {t1} {u1} in celcius scale and {t2} {u2} in fahrenhiet scale")

elif unit=="C":
    te1=temprature-273 
    t1=round(te1,1)
    te2=1.8*(temprature)+32
    t2=round(te2,1)
    u1="K"
    u2="F"
    print(f"given tempature is {t1} {u1} in kelvin scale and {t2} {u2} in fahrenhiet scale")

elif unit=="F":
    te1=(temprature-32)/1.8+273
    t1=round(te1,1)
    te2=(temprature-32)/1.8
    t2=round(te2,1)
    u1="K"
    u2="°C"
    print(f"given tempature is {t1} {u1} in kelvin scale and {t2} {u2} in celcius scale")


else:
    print(f"{unit} is not a valid unit")




