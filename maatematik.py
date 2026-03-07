def carpim_tablosu():
    sayi = int(input("Sayı: "))
    for i in range(1, 11):
        print(f"{sayi} x {i} = {sayi * i}")

def ritmik_sayma():
    bas = int(input("Başlangıç: "))
    bit = int(input("Bitiş: "))
    artis = int(input("Artış: "))
    for i in range(bas, bit + 1, artis):
        print(i)

def not_hesaplama():
    vize = float(input("Vize: "))
    final = float(input("Final: "))
    ort = vize * 0.4 + final * 0.6
    print("Ortalama:", ort)