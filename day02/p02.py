# Didalam ini kita akan belajar ttg
# A. Percabangan (en: branching)
# B. Ruang lingkup akses (en: variable scope)
# C. Pengulangan (en: loop)


# A. Percabangan

# A.1 Ini adalah struktur percabangan
umur = 17

kondisi = (umur == 1)

if (kondisi):  # if(kondisi) dapat dipersingkat menjadi 'if(umur == 1)'. Cara ini disebut 'inline'
    # jika benar (True)
    print("Umur anda 17")
else:
    # jika salah (False)
    print("Umur anda bukan 17")

# P1?: Rubah kode diatas sehingga kondisinya menjadi lebih muda dari 17 tahun dan dari mulI 17 tahun sampe lebih tua.

# A.2 Percabangan bisa dirangkai menjadi dengan percabangan lain (percabangan dalam percabangan)
tempat_lahir = "Jakarta"
punya_ktp = False

if (kondisi):
    print("Umur anda 17")
    punya_ktp = True

    if (tempat_lahir == "Jakarta"):
        punya_ktp_jakarta = True
        print("Umur 17 dan lahir di Jakarta")
    else:
        print("Umur 17 dan bukan lahir di Jakarta")
        punya_ktp_jakarta = False
else:
    # jika salah (False)
    print("Umur anda bukan 17")

# P2? Lihat contoh soal dibawah, apakah ada cara untuk menyederhanakan kode dibawah
#     (petunjuk: mungkin menggunakan syntax yang lain)

# kota = ""
# if(kota == "Aceh"):
#    ...
# if(kota == "Yogyakarta"):
#    ...
# if(kota == "Jakarta"):
#    ...

# P3? Rubah 'if clause' dibawah menjadi syntax yang anda usulkan

# B. Percabangan juga mempunyai ruang lingkup dari variable (en:variable scope).
# P4?: Apa yang di tampilan di layar apabila :
#       1. umur = 17 dan tempat_lahir = jakarta
#       2. umur = 16 dan tempat_lahir = jakarta
#       3. umur = 17 dan tempat_lahir = bandung
#       4. umur = 16 dan tempat_lahir = bandung

# P5?: Jelaskan dan berikan alasan dari jawaban anda.


# C. Pengulangan
# Ada beberapa macam pengulangan, salah satunya adalah "For loop".
# for x in range(1:10)                          -> nilai x dari 1 sampai 9
# for buah in ["pisang", "jambu", "mangga"]

# perintah dibawah akan mencetak # ke bawah sebanyak 10 kali
for x in range(1, 10):
    print("index: %s - #" % x)

# p6? rubah kode diatas untuk menampilkan # kesamping menjadi "##########"
# (petunjuk: yang menyebabkan karakter dicetak kebawah adalah 'newline')

for item in ["banana", "cherry"]:
    print(item)

# p7? bagaimana cara untuk keluar dari for..loop setelah mencetak kata (en:str) "pisang"

# P8? hasil dari perintah dibawah ini dan jelaskan ?
#     print("x : %s" % x)
#     print("x : %s" % item)
