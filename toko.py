print("============PECEL LELE============")
Pembeli = input("Nama Pembeli : ")
print("Nama Pembeli : ")

def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n=============MENU MAKANAN=============")
    print("1. Nasi Ayam Goreng - Rp.10000,00")
    print("2. Nasi Ayam Bakar - Rp.12000,00")
    print("3. Nasi Lele Goreng - Rp.11000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3 : "))
    porsi = int(input("Berapa Porsi : "))

    if nomor == 1:
        totalmakanan = porsi * 10000
        print(porsi, ' Nasi Ayam Goreng = Rp.',totalmakanan)
        makan=("Nasi Ayam Goreng")
    elif nomor == 2:
        totalmakanan = porsi * 12000
        print(porsi, ' Nasi Ayam Bakar = Rp.',totalmakanan)
        makan=("Nasi Ayam Bakar")
    elif nomor == 3:
        totalmakanan = porsi * 11000
        print(porsi, ' Nasi Lele Goreng = Rp.',totalmakanan)
        makan=("Nasi Lele Goreng")
    else:
        print("Pilihan tidak ada dalam daftar menu\nSilahkan pilih kembali!")
        makanan()

def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n=============MENU MINUMAN=============")
    print("1. Es Teh Manis - Rp.4000,00")
    print("2. Es Jeruk - Rp.6000,00")
    print("3. Jus Alpukat - Rp.7000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3 : "))
    gelas = int(input("Berapa Gelas : "))

    if nomor == 1:
        totalminuman = gelas * 4000
        print(gelas, ' Es Teh Manis = Rp.',totalminuman)
        minum=("Es Teh Manis")
    elif nomor == 2:
        totalminuman = gelas * 6000
        print(gelas, ' Es Jeruk = Rp.',totalminuman)
        minum=("Es Jeruk")
    elif nomor == 3:
        totalminuman = gelas * 7000
        print(gelas, ' Jus Alpukat = Rp.',totalminuman)
        minum=("Jus Alpukat")
    else:
        print("Pilihan tidak ada dalam daftar menu\nSilahkan pilih kembali!")
        minuman()

makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("\nTotal yang harus di bayar : ", total_semua)
uang = int(input("Uang Tunai Pemesan : Rp."))
kembalian = int(uang - total_semua)
print("Kembalian :", kembalian)

print("\n=================S T R U K B E L I=================")
print("Nama\t\t:",Pembeli)
print("Beli\t\t:",porsi,makan,"(Rp.",totalmakanan,")")
print("\t\t:",gelas,minum,"(Rp.",totalminuman,")")
print("Tagihan\t\t:Rp.",total_semua)
print("Dibayar\t\t: Rp.",uang)
print("Kembalian\t: Rp.",kembalian)



print("===================================================")
print("===================================================")