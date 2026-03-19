def hesapmakine():
    from hesapmakinesi.hesap_toplama import toplama
    from hesapmakinesi.hesap_cikarma import cikarma
    from hesapmakinesi.hesap_carpma import carpma
    from hesapmakinesi.hesap_bolme import bolme
    from hesapmakinesi.hesap_karekok import karekok
    from hesapmakinesi.hesap_mutlak import mutlak
    from hesapmakinesi.hesap_dairealan import dairealan
    from hesapmakinesi.hesap_dikdortgenalan import dikdortgen
    
    
    print("╔════════════════════════════╗")
    print("║\n===  Hesap Makinesi  ===\n╣")
    print("╠════════════════════════════╣")
    print("║   1- Toplama               ║")
    print("║   2- Çıkarma               ║")
    print("║   3- Çarpma                ║")
    print("║   4- Bölme                 ║")
    print("║   5- Karekök               ║")
    print("║   6- Mutlak                ║")
    print("║   7- Daire alan            ║")
    print("║   8- Dik dörtgen alan      ║")
    print("║   9- Çıkış                 ║")
    print("╚════════════════════════════╝")

    secim = input("Seçim: ")

    if secim == "1":
            toplama()
    elif secim == "2":
            cikarma()
    elif secim == "3":
            carpma()
    elif secim == "4":
            bolme()
    elif secim == "5":
            karekok()
    elif secim == "6":
        mutlak()
    elif secim == "7":
        dairealan()
    elif secim == "8":
        dikdortgen() 
    elif secim == "9":
        print("Çıkılıyor...")
        # break
    else:
        print("Geçersiz seçim!")
