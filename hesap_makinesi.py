def hesap_makinesi():
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
            print("Sonuç:", a / b if b != 0 else "Sıfıra bölme hatası!")
        else:
            print("Geçersiz işlem!")
    except:
        print("Hatalı giriş!")