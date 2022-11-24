daftar = str(input("Masukkan Daftar Pesanan : "))
pesanan = [daftar]
print("Daftar pesanan : ",pesanan)

pesanan_baru = str(input("Masukkan pesanan yang ingin ditambahkan : "))
if pesanan_baru in daftar:
    print(pesanan_baru.upper(), "sudah berada dalam pesanan")
else:
    daftar2 = [daftar, pesanan_baru]
    print(daftar2)
