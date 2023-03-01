print("="*20, "BARIS ARITMATIKA", "="*20)
bilangan_awal = int(input("Masukkan bilangan awal : "))
selisih_bilangan = int(input("Masukkan selisih bilangan : "))
jumlah_suku = int(input("Masukkan banyaknya suku : "))

def aritmatika(bilangan_awal, selisih_bilangan, jumlah_suku):
    total = jumlah_suku/2 * (2 * bilangan_awal + (jumlah_suku -1) * selisih_bilangan)
    return total

print("Total dari deret aritmatika tersebut adalah : ", aritmatika(bilangan_awal, selisih_bilangan, jumlah_suku))