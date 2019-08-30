# Ini adalah aplikasi sederhana proses pebuatan SIM.
# Anda bisa menjalankan aplikasi ini di pycharm dengan :
# 1. menekan tombol hijau play disamping kode (en: code) 'if __name__ == "__main__":'.
# 2. memilih "run -> run p02" pada menu pycharm.

# Tugas anda :
# 1. Sesusai peraturan kepolisian indonesia, batas umur paling bawah ada 17 tahun.
# 1.1 Rubah kode anda untuk menerima aplikasi orang berumur 17 tahun.
# 1.1 Hapus komentar (en: uncomment) test pada file 'hw03_test.py' baris 12.
#     Dan jalankan dengan "run -> p02_test. Test harus jalan tanpa gagal.
#
# 2. Apabila berkas belum terkirim maka orang tidak bisa mendapatkan SIM,
# 2.1 Rubah aplikasi ini sehingga hanya user menerima sim setelah berkas sudah dikirim.
# 2.2 Sertakan pesan 'berkas belum dikirim' apabila pengguna (en: user) belum mengirimkan aplikasi.
# 2.3 Pesan penolakan harus mempunyai struktur 'Alasan : [pesan]'
#     [pesan] = umur < 17 tahun
#     [pesan] = berkas belum dikirim
#     [pesan] = umur < 17 tahun dan berkas belum dikirim
# 2.4 _uncomment_ baris 'hw03_test.py' baris 10, 13 dan 16 lalu jalankan semua test yang ada.
#     Semua test harus berjalan tanpa ada kegagalan dalam test (en: assertion error).
#
# 3. Anda tidak boleh merubah kode didalam tests/hw03_test.py. Jalankan test tersebut untuk memvalidasi apakah jawaban
#       anda benar.

def membuat_sim(nama, umur, berkas_dikirim):
    mendapat_sim = umur > 17

    # syntax not adalah cara untuk menegasikan data bertipe boolean.
    # not(True) = False
    # not(False) = True
    if mendapat_sim:
        return "%s mendapatkan SIM A." % nama
    else:
        return "%s tidak mendapatkan SIM A. Alasan : %s." % (nama, "umur < 17 tahun")


def to_bool(value):
    # biasakan untuk menyertakan sumber tautan apabila anda mengambil sepotong kode dari manapun di internet.
    """
       Converts 'something' to boolean. Raises exception for invalid formats
           Possible True  values: 1, True, "1", "TRue", "yes", "y", "t"
           Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
       https://stackoverflow.com/questions/715417/converting-from-a-string-to-boolean-in-python
    """
    if str(value).lower() in ("Y", "y"):
        return True

    if str(value).lower() in ("T", "t"):
        return False

    raise Exception('Invalid value for boolean conversion: ' + str(value))


if __name__ == "__main__":
    nama = input("Masukan nama anda : ")

    umur = input("Masukan umur anda : ")

    print("Nama saya :%s dan umur %s", (nama, umur))

    berkas_dikirim = to_bool(input("Apakah berkas sudah dikirim ? [Y/T] : "))

    status_sim = membuat_sim(nama, int(umur), berkas_dikirim)

    print("Status pembuatan sim : %s, " % status_sim)
