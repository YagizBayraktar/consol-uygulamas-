def bolme():
    sayi1 = float(input("1. sayıyı gir: "))
    sayi2 = float(input("2. sayıyı gir: "))

    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("Sonuç:", sonuc)
    else:
        print("Bir sayı 0'a bölünemez.")