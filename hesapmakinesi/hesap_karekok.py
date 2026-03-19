def karekok():
    import math

    sayi = float(input("Bir sayı gir: "))

    if sayi >= 0:
        sonuc = math.sqrt(sayi)
        print("Karekök:", sonuc)
    else:
        print("Negatif sayının gerçek karekökü yoktur.")