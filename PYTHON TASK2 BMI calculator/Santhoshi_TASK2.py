# bmi calculator task 2
#user inputs tiskovali frst
weight = float(input("enter your weight in kg: "))
height_centimeters = float(input("enter your height in cm:"))

#height ni cm nundi m ki change cheyali
#formula 
height_meters=height_centimeters/100

#bmi calculate formula
#formula apply cheyska round apply cheystham 
bmi = weight/(height_meters**2)
#bmi formula
bmi = round(bmi,2)

#result printing
print(f"\nyour bmi value:{bmi}")

# health category chech cheydhm
''' below 18.5-underweight
18.5-24.9 normal weight
25.0-29.9 over weight
30.0 or above:obese '''
# epudu if else elif satements vadudham
if bmi<18.5:
    print("cateory: underweight")
elif 18.5 >= bmi <24.9:
    print("category: normal weight")
elif 25.0 >= bmi <29.9:
    print("category: over weight")
else:
    print("category:obese(need more care)")




