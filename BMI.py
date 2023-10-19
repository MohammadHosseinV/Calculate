from colorama import Fore

def BMI(Weight , height):
    result = Weight / (height ** 2)
    return f"{Fore.BLUE}  {result * 10000}"

print(BMI(79 ,184))

# Mohammad Hossein Habibpour