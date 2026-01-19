print("APLIKASI MENGHITUNG LUAS DAN KELILING BANGUN DATAR")

nama = input("Masukkn nama anda: ")
print("hello", nama)
print("dalam aplikasi ini, untuk menghitung luas dan keliling bngun datar")

#menampilkan daftar bangun datar
#menggunakan list.py
BangunDatar = ["1 persegi panjang", "2 persegi", "3 segitiga", "4 lingkaran"]
print("bangun datar")

# menggunakan fungsi (def)
def persegi_panjang():
    print("anda memilih persegi panjang")
    panjang = float(input("masukkan panjang persegi panjang: "))
    lebar = float(input("masukkan lebar persegi panjang: "))
    luas = panjang * lebar 
    keliling = 2 * (panjang + lebar )
    print("luas persegi panjang:", luas)
    print("keliling persegi panjang:", keliling)
def persegi() :
    print("anda memilih persegi ")
    sisi =  float(input("masukkan sisi persegi: "))   
    luas = sisi * sisi
    keliling = 4 * sisi
    print("luas persegi: ",luas)
    print("keliling persegi:",keliling)
def segitiga() :
    print("anda memilih segitiga ")
    alas =  float(input("masukkan alas segitiga: "))   
    tinggi = float(input("masukkan tinngi persegi: "))
    sisi_miring = (alas**2 + tinggi**2)**0,5
    luas = 0,5 * alas * tinggi
    keliling = alas * tinggi * sisi_miring
    print("luas segitig:", luas)
    print("keliling segitiga:", keliling)
def lingkaran() :
    print("anda memilih lingkarang")
    jari_jari = float(input("masukan jri-jari lingkarang: "))
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    print("luas lingkaran:",luas)
    print("keliling lingkaran:", keliling)

# meminta pengguna memilih bngun datar yang terdaftar dan akan dihitung luas dengan kelilingnya 
# menggunakan controlflow percabangan ( if-elif-else)
pilih = input("Silahkan Pilih Bangun Datar (1-4)")
if pilih == "1": 
    persegi_panjang()
elif pilih == "2":
    persegi()
elif pilih == "3":
    segitiga()
elif pilih == "4":
    lingkaran()
else:
    print("input tidak valid. silahkan pilih bangun datar dari 1-4,")

#bertanya ke user mau hitung lagi atau tidak, kalok lagi programya akan jalan lagi kalau tidak ucapkan terimakasih dengan perulangan while
while True:
    hitung_lagi = input("apakah kita ingin menghitung lagi? (ya atau tidak): ")
    if hitung_lagi == "iya":
        pilih = input("silahkan pilih bangun datar (1-4); ")
        if pilih == "1":
            persegi_panjang()
        elif pilih == "2":
            persegi()
        elif pilih == "3":
            segitiga()
        elif pilih == "4":
            lingkaran()
        else:
            print("input tidak valid. silahkan pilih bangun datar dari 1-4,")
    elif hitung_lagi == "tidak":
        print("okey thangks you telah menggunakan aplikasi ini:)")
        break
    else:
        print("input tidak valid. silahkan pilih bangun datar dari 1-4,")


            
            
            
            
            