kumpulan_bilangan = list(input("Masukkan sekumpulan bilangan (pisahkan dengan koma): ").split(","))
kumpulan_baru = []

for angka in kumpulan_bilangan :
    bilangan_baru = int(angka)
    kumpulan_baru.append(bilangan_baru)

bilangan_terbesar = lambda kumpulan_baru : max(kumpulan_baru, key = int)
bilangan_terkecil = lambda kumpulan_baru : min(kumpulan_baru, key = int)

print ("Bilangan terbesar dari kumpulan bilangan yang di input adalah", bilangan_terbesar(kumpulan_baru))
print ("Bilangan terkecil dari kumpulan bilangan di input adalah", bilangan_terkecil(kumpulan_baru))