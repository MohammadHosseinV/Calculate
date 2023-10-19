def BMI(Weight , height):
    result = Weight / (height ** 2)
    return result * 10000

print(BMI(79 ,184))