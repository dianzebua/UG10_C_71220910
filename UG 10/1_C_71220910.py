print ("=========== Pilih Menu =============")
print ("1. Tambah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")

bilangan_pertama = int(input("Masukkan angka pertama : "))
bilangan_kedua = int(input("Masukkan angka kedua : ")) 
Pilihan = input("Pilihan anda : ")
if Pilihan == "1":
    hasil = bilangan_pertama+bilangan_kedua
    print ("hasil : ", hasil)
elif Pilihan == "2":
    hasil = bilangan_pertama-bilangan_kedua
    print ("hasil : ", hasil)
elif Pilihan == "3":
    hasil = bilangan_pertama*bilangan_kedua
    print ("hasil : ", hasil)
elif Pilihan == "4":
    hasil = bilangan_pertama/bilangan_kedua
    print ("hasil : ", hasil)
else :
    print ("error!")
