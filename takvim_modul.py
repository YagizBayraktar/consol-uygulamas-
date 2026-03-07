import datetime

def bugun():
    now = datetime.datetime.now()
    print("Tarih:", now.strftime("%d-%m-%Y"))
    print("Saat:", now.strftime("%H:%M:%S"))