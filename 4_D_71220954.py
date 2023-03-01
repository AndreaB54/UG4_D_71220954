kumpulan_bilangan = input("Masukkan sekumpulan bilangan (pisahkan dengan koma): ").split(",")

bilangan_terbesar = lambda kumpulan_bilangan : max(kumpulan_bilangan, key = len)
bilangan_terkecil = lambda kumpulan_bilangan : min(kumpulan_bilangan, key = len)

print ("Bilangan terbesar dari kumpulan bilangan yang di input adalah", bilangan_terbesar(kumpulan_bilangan))
print ("Bilangan terkecil dari kumpulan bilangan di input adalah", bilangan_terkecil(kumpulan_bilangan))