from hesap_makinesi import hesap_makinesi
from oyunlar import sayi_tahmin
from sekil import ucgen
from takvim_modul import bugun
from matematik import carpim_tablosu, ritmik_sayma, not_hesaplama
from donusum import bmi, sicaklik, doviz

while True:
    print("╔════════════════════════════╗)
    print("║\n===    Prpje Görevi    ===╣")
    print("╠════════════════════════════╣")
    print("║   1- Hesap Makinesi        ║")
    print("║   2- Oyun                  ║")
    print("║   3- Şekil Çiz             ║")
    print("║   4- Takvim                ║")
    print("║   5- Ritmik Sayma          ║")
    print("║   6- Not Hesaplama         ║")
    print("║   7- Çarpım Tablosu        ║")
    print("║   8- BMI                   ║")
    print("║   9- Döviz                 ║")
    print("║   10- Sıcaklı              ║")
    print("║   11- Çıkış                ║")
    print("╚════════════════════════════╝")

    secim = input("Seçim: ")

    if secim == "1":
        hesap_makinesi()
    elif secim == "2":
        sayi_tahmin()
    elif secim == "3":
        ucgen()
    elif secim == "4":
        bugun()
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
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")