masukkan_kalimat = str(input("Masukkan sebuah kalimat: ")).split()

def kata_terpanjang (masukkan_kalimat):
    hitung_kata = max(masukkan_kalimat, key = len)
    return hitung_kata
print ("Kata terpanjang dalam kalimat tersebut adalah: ", kata_terpanjang(masukkan_kalimat))