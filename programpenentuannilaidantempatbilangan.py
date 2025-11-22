# program penentuan Nilai Tempat Bilangan
# menggunakan fungsi try_expect untuk menangani kesalahan (eror), jika user input  selain angka 
print("\nAPLIKASI PENENTUAN NILAI DAN TEMPAT BILANGAN")
# meminta input bilangan dari user
try:
    angka = int(input("\nMasukan Bilangan (maksimmal 9 digit) : "))

    # penentuan nilai tempat dari ratusan juta sampai satuan
    if 0 <= angka <= 999999999:

        # ambil nilai ratusan juta 
        ratusanjuta = angka  // 100000000
        # hitung sisa setelah ratusan juta diambil
        sisaratusanjuta = angka % 100000000

        # ambil nilai puluhan juta dari sisa ratusan juta
        puluhanjuta = sisaratusanjuta // 10000000
        # hitung sisa seetelah puluhan juta diambil 
        sisapuluhanjuta = sisaratusanjuta % 10000000

        # ambil nilai jutaan dari sisa puluhan juta
        jutaan = sisapuluhanjuta // 1000000
        # hitung sisa jutaan
        sisajutaan = sisapuluhanjuta % 1000000

        # ambil nilai ratusan ribu dari sisa jutaan
        ratusanribu = sisajutaan // 100000
        # hitung sisa setelah ratusanribu diambil
        sisaratusanribu = sisajutaan % 100000

        # ambil nilai puluhan ribu dari sisa rartusan ribu 
        puluhanribu = sisaratusanribu // 10000
        # hitung sisa setelah puluhanribu diambil
        sisapuluhanribu = sisaratusanribu % 10000

        # ambil nilai ribuan dari puluhan ribu
        ribuan = sisapuluhanribu // 1000
        # hitung sisa setelah diambil ribuan
        sisaribuan = sisapuluhanribu % 1000

        # ambil nilai ratusan dari sisa ribuan
        ratusan = sisaribuan // 100
        # hitung sisa setelah diambil ratusanyya
        sisaratusan = sisaribuan % 100

        # ambil nilai puluhan dari sisa ratusan 
        puluhan = sisaratusan // 10
        # sisa terakhir adalah satuan 
        satuan = sisaratusan % 10

    # menampilkan hasil sesuai dengan nilai tempat 
        print(f"\nAnda memasukan bilangan {angka} dimana:")
        print(f"{ratusanjuta} merupakan ratusanjuta")
        print(f"{puluhanjuta} merupakan puluhanjuta")
        print(f"{jutaan} merupakan jutaan")
        print(f"{ratusanribu} merupakan ratusanribu")
        print(f"{puluhanribu} merupakan puluhanribu") 
        print(f"{ribuan} merupakan ribuan")
        print(f"{ratusan} merupak ratusan")
        print(f"{puluhan} merupakan puluhan")
        print(f"{satuan} merupakan satuan")

    else:
        print("Harap memasukkan bilangan antara 0-999999999.")

except ValueError: 
    print("input tidak valid! Harap masukan angka.")


 

        


