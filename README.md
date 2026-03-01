import datetime
import random

def hesap_makinesi():
    print("\n--- HESAP MAKİNESİ ---")
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        islem = input("İşlem (+, -, *, /): ")

        if islem == "+":
            print("Sonuç:", a + b)
        elif islem == "-":
            print("Sonuç:", a - b)
        elif islem == "*":
            print("Sonuç:", a * b)
        elif islem == "/":
            if b != 0:
                print("Sonuç:", a / b)
            else:
                print("Sıfıra bölme hatası!")
        else:
            print("Geçersiz işlem!")
    except:
        print("Hatalı giriş yaptınız!")


def oyun():
    print("\n--- SAYI TAHMİN OYUNU ---")
    sayi = random.randint(1, 10)
    tahmin = int(input("1-10 arasında tahmin yap: "))
    if tahmin == sayi:
        print("🎉 Doğru bildin!")
    else:
        print("Yanlış! Doğru sayı:", sayi)


def sekil_ciz():
    print("\n--- ŞEKİL ÇİZDİRME ---")
    satir = int(input("Satır sayısı: "))
    for i in range(1, satir + 1):
        print("*" * i)


def takvim():
    print("\n--- TAKVİM ---")
    bugun = datetime.datetime.now()
    print("Bugünün tarihi:", bugun.strftime("%d-%m-%Y"))
    print("Saat:", bugun.strftime("%H:%M:%S"))


def ritmik_sayma():
    print("\n--- RİTMİK SAYMA ---")
    bas = int(input("Başlangıç: "))
    bit = int(input("Bitiş: "))
    artis = int(input("Artış miktarı: "))
    for i in range(bas, bit + 1, artis):
        print(i)


def not_hesaplama():
    print("\n--- NOT HESAPLAMA ---")
    vize = float(input("Vize notu: "))
    final = float(input("Final notu: "))
    ort = vize * 0.4 + final * 0.6
    print("Ortalama:", ort)
    if ort >= 50:
        print("Geçtiniz ✅")
    else:
        print("Kaldınız ❌")


def carpim_tablosu():
    print("\n--- ÇARPIM TABLOSU ---")
    sayi = int(input("Hangi sayının çarpım tablosu?: "))
    for i in range(1, 11):
        print(f"{sayi} x {i} = {sayi * i}")


def bmi():
    print("\n--- BMI HESAPLAMA ---")
    kilo = float(input("Kilo (kg): "))
    boy = float(input("Boy (metre): "))
    indeks = kilo / (boy ** 2)
    print("BMI:", round(indeks, 2))


def doviz():
    print("\n--- DÖVİZ UYGULAMASI ---")
    tl = float(input("TL miktarı: "))
    kur = 32  # sabit örnek kur
    print("USD karşılığı:", tl / kur)


def sicaklik():
    print("\n--- SICAKLIK ÇEVİRME ---")
    c = float(input("Celsius değeri: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)


while True:
    print("\n╔== Consol Uygulaması ==═╗")
    print("║  1- HESAP MAKİNESİ      ║")
    print("║  2- OYUNLAR             ║")
    print("║  3- ŞEKİL ÇİZDİRME      ║")
    print("║  4- TAKVİM              ║")
    print("║  5- RİTMİK SAYMA        ║")
    print("║  6- NOT HESAPLAMA       ║")
    print("║  7- ÇARPIM TABLOSU      ║")
    print("║  8- BMI HESAPLAMA       ║")
    print("║  9- DÖVİZ UYGULAMASI    ║ ")
    print("║  10- SICAKLIK ÇEVİRME   ║ ")
    print("║  11- ÇIKIŞ              ║ ")
    print("╚═════════════════════════╝")

    secim = input("Seçiminiz: ")

    if secim == "1":
        hesap_makinesi()
    elif secim == "2":
        oyun()
    elif secim == "3":
        sekil_ciz()
    elif secim == "4":
        takvim()
    elif secim == "5":
        ritmik_sayma()
    elif secim == "6":
        not_hesaplama()
    elif secim == "7":
        carpim_tablosu()
    elif secim == "8":
        bmi()
    elif secim == "9":
        doviz()
    elif secim == "10":
        sicaklik()
    elif secim == "11":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim yaptınız!")
