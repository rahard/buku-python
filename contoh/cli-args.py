# contoh parsing argumen yang diberikan kepada program
# beri nama skrip ini cli-args.py
# cara menjalankan:
#    python3 cli-args.py opsi1 opsi2 opsi3 
# opsi bisa banyak

import sys
# periksa jumlah argumennya

numberargs = len(sys.argv)
# tanpa argumen, hasilnya akan 0 (nol)
# nama skrip adalah sys.argv[0]

# print argumen yang diberikan
for i in range(numberargs):
   print(i, sys.argv[i])

