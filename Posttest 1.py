Cnama = input("Masukan Nama : ")
Cnim = int(input("Masukan Nim :"))
Cpass = input("Masukan Pass: ")

if Cnama == "fatiematul" and Cnim == 2399016010 and Cpass == "password":
    print("Menentukan Volume Ruang Bangun")
    print("1.Bola")
    print("2.Tabung")
    print("3.Limas Segitiga")
    pi = 22/7
    Pilihan = int(input("Masukan Pilihan Menu: "))
    if Pilihan == 1:
        jari = int(input("Masukan jari : "))
        volume = 4/3*pi*(jari*jari*jari) 
        print("Volume Bola : ",volume )
    elif Pilihan == 2:
        jari = int(input("Masukan jari : "))
        tinggi = int(input("Masukan tinggi : "))
        volume = pi*(jari*jari)*tinggi
        print("volume tabung : ",volume)
    elif Pilihan == 3:
        luasAlas = int(input("Masukan luas alas : "))
        tinggiLimas = int(input("Masukan tinggi limas : "))
        volume = 1/3*luasAlas*tinggiLimas
        print("volume limas segitiga : ",volume)
    else:
        print("pilihan tidak tersedia")
