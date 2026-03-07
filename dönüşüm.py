def bmi():
    kilo = float(input("Kilo: "))
    boy = float(input("Boy: "))
    print("BMI:", kilo / (boy ** 2))

def sicaklik():
    c = float(input("Celsius: "))
    print("Fahrenheit:", (c * 9/5) + 32)

def doviz():
    tl = float(input("TL: "))
    kur = 44.07
    print("USD:", tl / kur)