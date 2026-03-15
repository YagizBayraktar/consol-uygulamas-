def anasekil():    
        from sekil.sekil_cicek import cicek
        from sekil.sekil_mandala import mandala
        from sekil.sekil_patlama  import patlama
        from sekil.sekil_spirial import spirial
        from sekil.sekil_Spirograph import spirograph
        from sekil.sekil_ucgen import ucgen

        print("╔════════════════════════════╗")
        print("║\n===    şekiller      ===\n╣")
        print("╠════════════════════════════╣")
        print("║   1- çiçek                 ║")
        print("║   2- mandala               ║")
        print("║   3- patlama               ║")
        print("║   4- spiral                ║")
        print("║   5- spirograph            ║")
        print("║   6- ucgen                 ║")
        print("║   7- Çıkış                 ║") 
        print("╚════════════════════════════╝") 

        secim = input("Seçim: ")
        if secim == "1":
            cicek()
        elif secim == "2":
            mandala()
        elif secim == "3":
            patlama()
        elif secim == "4":
            spirial()
        elif secim == "5":
            spirograph()
        elif secim == "6":
            ucgen()
        elif secim == "7":
            print("Çıkılıyor...")
        else:
            print("Geçersiz seçim!")