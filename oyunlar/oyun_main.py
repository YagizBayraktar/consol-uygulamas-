def oyunmenusu():
    from oyunlar.oyun_adamasmaca import adamasmaca
    from oyunlar.oyun_taskagitmakas import taskagitmakas
    from oyunlar.oyun_sayitahmin  import sayitahmin
    from oyunlar.oyun_yılanoyunu import yılanoyunu
    from oyunlar.oyun_blokoyunu import blokoyunu
    from oyunlar.oyun_mayıntarlası import mayıntarlası

    print("╔════════════════════════════╗")
    print("║\n===    oyunlar       ===\n╣")
    print("╠════════════════════════════╣")
    print("║   1- Adam asmaca           ║")
    print("║   2- Taş kağıt makas       ║")
    print("║   3- Sayı tahmin           ║")
    print("║   4- Yılan oyunu           ║")
    print("║   5- Blok oyunu            ║")
    print("║   6- Mayın tarlası         ║")
    print("║   7- Puzzle                ║")
    print("║   8- Çıkış                 ║") 
    print("╚════════════════════════════╝") 

    secim = input("Seçim: ")

    if secim == "1":
        adamasmaca()
    
    elif secim == "2":
        taskagitmakas()
    elif secim == "3":
        oyun_sayitahmin()
    elif secim == "4":
        oyun_yılanoyunu()
    elif secim == "5":
        oyun_blokoyunu()
    elif secim == "6":
        oyun_mayıntarlası()
    elif secim == "7":
        oyun_puzzle()
    elif secim == "8":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")