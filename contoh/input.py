
# ini untuk Python 2.7
# gunakan raw_input
nama = raw_input("Masukkan nama Anda: ")
print "Selamat pagi,", nama

# for loop bisa menggunakan elemen dari string
# tidak harus indeks angka
for i in nama:
    print i

# associative array: hitung jumlah huruf dan spasi
huruf = {}  # inisialisasi
for key in nama:
    if key in huruf:
        huruf[key] += 1
    else:
        huruf[key]=1
# tampilkan hasil python 2.7
# sorted() agar key-nya diurutkan
# for python 3.* use this: for key, value in d.items():
for key, value in sorted(huruf.iteritems()):
    print key, value
