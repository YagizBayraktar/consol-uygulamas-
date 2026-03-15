import random

def sayitahmin():
    sayi = random.randint(1, 10)
    tahmin = int(input("1-10 arası tahmin: "))
    if tahmin == sayi:
        print("Kazandın!")
    else:
        print("Kaybettin! Doğru sayı:", sayi)