#latihan list (daptar)
#list itu tipe data yang digunakan untuk menyimpan banyak data dalam satu variabel.
#python list menggunakan kurung siku []


mobil= ["pajero", "bmw", "bugati", "lamborghini", "ferrari", "avanza"]
#index     0        1        2           3             4          5
print(mobil[0])
print(mobil[1])
print(mobil[2])
print(mobil[3])
print(mobil[4])
print(mobil[5])
#index negatip mulai menghiitung darri akhir
print(mobil[-3]) 
print(mobil[-2])

#LATIHAN MENGUBAH PYTHON LISTS
motor = ["yamaha", "honda", "vespa", "aerox", "NMAX"]
motor[3] = "kawasaki ninja 250"
print(motor)

# LATIHAN MENAMBAHKAN ITEM DI LISTS 
#untuk menambahkan item ke akhir daftar, gunakan append
mobil = ["bmw", "lamborghini", "ferrari", "pajero"]
mobil.append("bugatti chiron")
print(mobil)
#untuk menyisipkan item daptar pada index tertentu, gunakan insert
mobil = ["bmw", "lamborghini", "pajero", "bugati chiron"]
mobil.insert(2, "avanza")
print(mobil)

#LATIHAN MENGHAPUS ITEM DI LISTS
#utuk menghapus item yang ditentukan menggunakan remove
motor = ["yamaha", "honda", "aerox", "vespa", "nmax"]
motor.remove("aerox") 
print(motor)
#untuk mengosongkan lists menggunakan clear
motor = ["yamaha", "honda", "aerox", "vespa", "nmax"]
motor.clear() 
print(motor)

#LATIHAN PENGULANGAN ITEM DI LISTS 
#(---perulangan menggunakan for---)
#for digunakan untuk mencetak perulangan item daftar, satu persatu
warna = ["hitam", "putih", "biru", "merah", "abu", "dark"]
for y in warna:
  print(y)

#latihan pengulangan melalui nomor indeks.
#perulangan melalui item daftar dengan merujuk pada nomor indeksnya, menggunakan fungsi range()and len()
buah = ["kelengkeng", "mangga", "semangka", "pisang", "melon"]
for x in range(len(buah)):
  print(buah[x])

#(---perulangan menggunakan while---)
#while perulangan digunakan untuk menelusuri semua nomor indeks
nama = ["nazila", "hilmi", "safwah", "riza", "dewi", "wiliana"]
n = 0
while n < len(nama):
  print(nama[n])
  n = n + 1

#LATIHAN PEMAHAMAN DI ITEM LIST
#List comprehension menggunakn sintaks yang lebih singkat ketika ingin membuat daftar baru berdasarkan nilai nilai dari daftar yng sudah ada
#Berdasarkan daftar negara negara yang ada, kita mengiinginkn daftar baru yang hanya berisi negara negara yang namanya mengandung huruf "o"
#tanpa list comprehension, kita harus menulis for pernyataan dengan uji kondisional di dalamnya:
negara = ["jepang", "cina", "korea", "laos", "swiss", "yordania", "lebanon"]
newlist = []

for n in negara:
  if "o" in n:
    newlist.append(n)

print(newlist)

#Dengan list comprehension, kita dapat melakukan semua itu hanya dengan satu baris kode
negara = ["jepang", "cina", "korea", "laos", "swiss", "yordania", "lebanon"]

newlist = [n for n in negara if "o" in n]

print(newlist)

#LATIHAN MENGURUTKAN DAFTAR PYTHON LISTS
# Objek List memiliki method sort()
# Method sort() digunakan untuk mengurutkan isi list
# Secara default, pengurutan dilakukan secara alfanumerik dan menarik
# Artinya:
# - Jika isi list berupa teks (string), maka akan diurutkan berdasarkan alfabet (A - Z)
# - Jika isi list berupa angka, maka akan diurutkan dari nilai terkecil ke terbesar

# Membuat list yang berisi beberapa nama negara
negara = ["jepang", "cina", "belanda", "korea", "swiss", "amerika", "rusia"]
negara.sort()
print(negara)

#mebuat list yang berisis beberapa angka
angka = [100, 8, 11, 27, 90, 65, 32]
angka.sort()
print(angka)

#LATIHAN salin DAFTAR py
# untuk menyalin sebuah daftar, kita dapat menggunakan metode copy (), list() dan  operator slice
# kita tidak dapat menyalin daftar hanya dengan mengetik list2 = list1
# Karena list2 hanya akan menjadi referensi ke list1
# Artinya:
# - Perubahan yang dilakukan pada list1 juga akan secara otomatis mempengaruhi list2
# - Jadi list2 tidak benar-benar list baru, hanya nama lain untuk list yang sama

#Buat salinan daftar dengan copy()
desa = ["gerung", "suela", "toya", "rakam", "suralaga"]
desa2 = desa.copy()
print(desa2)

#membuat salinan dengan menggunakan metode list().
desa = ["gerung", "suela", "toya", "rakam", "suralaga"]
desa2 = list(desa)
print(desa2)

#LATIHAN MENGGABUNGKAN DUA LISTS PY
# Ada beberapa cara untuk menggabungkan atau menyatukan dua atau lebih list di Python

# menggabungkan, atau menyatukan, dua atau lebih daftar di Pytho nmenggunakan + operator
# Gabungkan dua daftar:
nama1 = ["nazila", "safwah", "aull", "hilmi"] #string
nama2 = ["jay", "jeno", "suno", "boboboy"] #string
nama3 = nama1 + nama2
print(nama3)

#cara lain untuk menggabungkan dua daftar dengan menambahkan semua item dari daftar2 ke daftar1, satu per satu:
nama1 = ["nazila", "safwah", "aull", "hilmi"]
nama2 = ["jay", "jeno", "suno", "boboboy"]

for x in nama2:
  nama1.append(x)

print(nama1)

#kita dapat menggunakan extend() metode, untuk  untuk menambahkan list2 di akhir list1:
nama1 = ["jay", "jeno", "suno", "boboboy"]
nama2 = ["nazila", "safwah", "aull", "hilmi"]

nama1.extend(nama2)
print(nama1)

# LATIHAN LIST METHODS ATAU DAFTAR METODE 
# List method adalah fungsi bawaan Python yang digunakan untuk mengubah, mengelola, atau mengambil data dari sebuah list
# contoh 

# APPEND() Fungsi: Menambahkan 1 elemen ke akhir list
mobil = ["bmw", "lamborghini", "ferrari", "pajero"]
mobil.append("bugatti chiron")
print(mobil)

# CLEAR() Fungsi: Menghapus semua isi list
motor = ["yamaha", "honda", "aerox", "vespa", "nmax"]
motor.clear() 
print(motor)

# COPY() Fungsi: Menyalin list ke list baru
desa = ["gerung", "suela", "toya", "rakam", "suralaga"]
desa2 = desa.copy()
print(desa2)

# COUNT() fungsi: Menghitung berapa kali suatu data muncul di lists
negara = ["jepang", "korea", "cina", "swiss", "cina", "belanda", "cina"]
print(negara.count("cina"))

# EXTEND() fungsi: untuk menambahkan (menggabungkan) semua isi list lain ke dalam sebuah list
# Kita dapat menggunakan metode extend() untuk menambahkan semua isi list2 ke akhir list1
# Isi list2 akan dimasukkan satu per satu ke dalam list1
nama1 = ["jay", "jeno", "suno", "boboboy"]
nama2 = ["nazila", "safwah", "aull", "hilmi"]

nama1.extend(nama2)
print(nama1)

# INDEX() fungsi: Mencari posisi (index) suatu nilai
negara = ["swisss", "cina","korea", "jepang", "amerika", "london"]
# index       0        1      2         3          4         5
print(negara.index("cina"))

# INSERT() fungsi: Menambahkan elemen di posisi tertentu
# untuk menyisipkan item daptar pada index tertentu, gunakan insert 
mobil = ["bmw", "lamborghini", "pajero", "bugati chiron"]
# index    0         1            2          3       4
mobil.insert(2, "avanza")
print(mobil)

# POP() Fungsi: Menghapus elemen berdasarkan index
phone = ["samsung", "iphone", "infinix", "oppo", "poco"]
# idex     0            2         3         4      5
phone.pop(3)
print(phone)

# REMOVE() fungsi: Fungsi: Menghapus elemen berdasarkan nilai
#utuk menghapus item yang ditentukan menggunakan remove
motor = ["yamaha", "honda", "aerox", "vespa", "nmax"]
motor.remove("aerox") 
print(motor)

# REVERSE() Fungsi: Membalik urutan elemen di dalam list
# Bukan menghitung atau “menomori dari belakang”, hanya membalik posisi setiap item
nama = ["jay", "kairi", "keyfer", "ceun woo", "jiang li"]
nama.reverse()
print(nama)





