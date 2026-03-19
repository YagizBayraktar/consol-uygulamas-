def bmi():
    kilo = float(input("Kilo: "))
    boy = float(input("Boy: "))
    print("BMI:", kilo / (boy ** 2))

def sicaklik():
    c = float(input("Celsius: "))
    print("Fahrenheit:", (c * 9/5) + 32)

import requests

# pip install requests yapmayı unutmayın

# Kullanıcının yazdığı isimleri kodlara çevirir
para_map = {
    "dolar": "USD",
    "amerikan doları": "USD",
    "usd": "USD",

    "euro": "EUR",
    "avro": "EUR",
    "eur": "EUR",

    "tl": "TRY",
    "try": "TRY",
    "türk lirası": "TRY",
    "turk lirasi": "TRY",

    "sterlin": "GBP",
    "ingiliz sterlini": "GBP",
    "gbp": "GBP",

    "yen": "JPY",
    "japon yeni": "JPY",
    "jpy": "JPY",

    "riyal": "SAR",
    "suudi riyali": "SAR",
    "sar": "SAR",

    "frank": "CHF",
    "isviçre frangı": "CHF",
    "isvicre frangi": "CHF",
    "chf": "CHF",

    "kanada doları": "CAD",
    "kanada dolari": "CAD",
    "cad": "CAD",

    "avustralya doları": "AUD",
    "avustralya dolari": "AUD",
    "aud": "AUD",
    "ruble": "RUB",
    "rus rublesi": "RUB",
    "rub": "RUB",

    "yuan": "CNY",
    "çin yuanı": "CNY",
    "cin yuani": "CNY",
    "cny": "CNY"
}

# Kodları gerçek isimlere çevirir
para_isim = {
    "USD": "Amerikan Doları",
    "EUR": "Euro",
    "TRY": "Türk Lirası",
    "GBP": "İngiliz Sterlini",
    "JPY": "Japon Yeni",
    "SAR": "Suudi Riyali",
    "CHF": "İsviçre Frangı",
    "CAD": "Kanada Doları",
    "AUD": "Avustralya Doları",
    "RUB": "Rus Rublesi",
    "CNY": "Çin Yuanı"
}


def para_kodu_bul(giris):
    return para_map.get(giris.strip().lower())


def kullanilabilir_paralar():
    print("\nKullanabileceğin para birimleri:")
    print("dolar, amerikan doları")
    print("euro, avro")
    print("tl, türk lirası")
    print("sterlin, ingiliz sterlini")
    print("yen, japon yeni")
    print("riyal, suudi riyali")
    print("frank, isviçre frangı")
    print("kanada doları")
    print("avustralya doları")
    print("ruble")
    print("yuan")


def anlik_tum_kurlar():
    print("\n=== 1 BİRİM DÖVİZ KAÇ TÜRK LİRASI? ===\n")

    try:
        url = "https://api.frankfurter.app/latest?from=TRY"
        veri = requests.get(url, timeout=10).json()

        if "rates" in veri:
            for para_birimi, deger in sorted(veri["rates"].items()):
                tl_karsiligi = 1 / deger
                para_adi = para_isim.get(para_birimi, para_birimi)
                print(f"1 {para_adi} = {tl_karsiligi:.4f} Türk Lirası")
        else:
            print("Veri alınamadı.")

    except:
        print("İnternet bağlantısı yok veya veri çekilemedi.")


def doviz_cevir():
    print("\n=== DÖVİZ ÇEVİRME ===")
    kullanilabilir_paralar()

    try:
        kaynak_giris = input("\nKaynak para birimi: ")
        hedef_giris = input("Hedef para birimi: ")
        miktar = float(input("Miktar: "))

        kaynak = para_kodu_bul(kaynak_giris)
        hedef = para_kodu_bul(hedef_giris)

        if not kaynak or not hedef:
            print("Geçersiz para birimi girdin.")
            return

        url = f"https://api.frankfurter.app/latest?from={kaynak}&to={hedef}"
        veri = requests.get(url, timeout=10).json()

        if "rates" in veri and hedef in veri["rates"]:
            kur = veri["rates"][hedef]
            sonuc = miktar * kur

            kaynak_adi = para_isim.get(kaynak, kaynak)
            hedef_adi = para_isim.get(hedef, hedef)

            print(f"\n1 {kaynak_adi} = {kur:.4f} {hedef_adi}")
            print(f"{miktar} {kaynak_adi} = {sonuc:.4f} {hedef_adi}")
        else:
            print("Dönüşüm yapılamadı.")

    except ValueError:
        print("Lütfen miktarı sayı olarak gir.")
    except:
        print("İnternet yok veya veri alınamadı.")


def populer_kurlar():
    print("\n=== POPÜLER KURLAR ===\n")

    try:
        url = "https://api.frankfurter.app/latest?from=TRY&to=USD,EUR,GBP,JPY,SAR"
        veri = requests.get(url, timeout=10).json()

        if "rates" in veri:
            for para_birimi, deger in sorted(veri["rates"].items()):
                tl_karsiligi = 1 / deger
                para_adi = para_isim.get(para_birimi, para_birimi)
                print(f"1 {para_adi} = {tl_karsiligi:.4f} Türk Lirası")
        else:
            print("Veri alınamadı.")

    except:
        print("İnternet yok veya veri alınamadı.")


def tl_den_dovize():
    print("\n=== TÜRK LİRASINDAN DÖVİZE ÇEVİRME ===")
    kullanilabilir_paralar()

    try:
        hedef_giris = input("\nHedef para birimi: ")
        miktar = float(input("Kaç Türk Lirası çevrilecek: "))

        hedef = para_kodu_bul(hedef_giris)

        if not hedef:
            print("Geçersiz para birimi girdin.")
            return

        url = f"https://api.frankfurter.app/latest?from=TRY&to={hedef}"
        veri = requests.get(url, timeout=10).json()

        if "rates" in veri and hedef in veri["rates"]:
            kur = veri["rates"][hedef]
            sonuc = miktar * kur

            hedef_adi = para_isim.get(hedef, hedef)

            print(f"\n1 Türk Lirası = {kur:.4f} {hedef_adi}")
            print(f"{miktar} Türk Lirası = {sonuc:.4f} {hedef_adi}")
        else:
            print("Dönüşüm yapılamadı.")

    except ValueError:
        print("Lütfen miktarı sayı olarak gir.")
    except:
        print("Veri alınamadı.")


def dovizden_tl():
    print("\n=== DÖVİZDAN TÜRK LİRASINA ÇEVİRME ===")
    kullanilabilir_paralar()

    try:
        kaynak_giris = input("\nKaynak para birimi: ")
        miktar = float(input("Miktar: "))

        kaynak = para_kodu_bul(kaynak_giris)

        if not kaynak:
            print("Geçersiz para birimi girdin.")
            return

        url = f"https://api.frankfurter.app/latest?from={kaynak}&to=TRY"
        veri = requests.get(url, timeout=10).json()

        if "rates" in veri and "TRY" in veri["rates"]:
            kur = veri["rates"]["TRY"]
            sonuc = miktar * kur

            kaynak_adi = para_isim.get(kaynak, kaynak)

            print(f"\n1 {kaynak_adi} = {kur:.4f} Türk Lirası")
            print(f"{miktar} {kaynak_adi} = {sonuc:.4f} Türk Lirası")
        else:
            print("Dönüşüm yapılamadı.")

    except ValueError:
        print("Lütfen miktarı sayı olarak gir.")
    except:
        print("Veri alınamadı.")


def doviz_menu():
    while True:
        print("\n==============================")
        print("         DÖVİZ MENÜSÜ")
        print("==============================")
        print("1- 1 Birim Döviz Kaç Türk Lirası")
        print("2- Döviz Çevir")
        print("3- Popüler Kurları Göster")
        print("4- Türk Lirasından Dövize Çevir")
        print("5- Dövizden Türk Lirasına Çevir")
        print("6- Çıkış")

        secim = input("Seçim: ")

        if secim == "1":
            anlik_tum_kurlar()
        elif secim == "2":
            doviz_cevir()
        elif secim == "3":
            populer_kurlar()
        elif secim == "4":
            tl_den_dovize()
        elif secim == "5":
            dovizden_tl()
        elif secim == "6":
            print("Döviz menüsünden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim yaptın.")