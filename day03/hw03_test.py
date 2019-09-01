import unittest
import hw03

from parameterized import parameterized


class TestMendapatkanSim(unittest.TestCase):

    @parameterized.expand([
        [16, "y", "%s tidak mendapatkan SIM A. Alasan : umur < 17 tahun."],
        # [16, "t", "%s tidak mendapatkan SIM A. Alasan : umur < 17 tahun dan berkas belum dikirim."],

        [17, "y", "%s mendapatkan SIM A."],
        # [17, "t", "%s tidak mendapatkan SIM A. Alasan : berkas belum dikirim."],

        [18, "y", "%s mendapatkan SIM A."],
        # [18, "t", "%s tidak mendapatkan SIM A. Alasan : berkas belum dikirim."]
    ])
    def test_mendapatkan_sim(self, umur, berkas_terkirim, text):
        nama = "Saya"

        expected_text = text % nama

        current_text = hw03.membuat_sim(nama, umur, hw03.to_bool(berkas_terkirim))

        self.assertEqual(expected_text, current_text, "Pesan tidak sesuai, algoritmanya masih salah")


if __name__ == '__main__':
    unittest.main()
