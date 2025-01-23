import pywhatkit
import pyautogui
import time
from datetime import datetime, timedelta

# Fungsi untuk mengirim pesan ke satu nomor
def kirim_pesan(nomor, pesan, jam, menit):
    try:
        pywhatkit.sendwhatmsg(nomor, pesan, jam, menit, wait_time=10)
        print(f"Pesan berhasil dikirim ke {nomor}")
        # Menutup tab WhatsApp Web yang terbuka setelah pesan terkirim
        time.sleep(10)
        pyautogui.hotkey('ctrl', 'w')  # Tutup tab
    except Exception as e:
        print(f"Terjadi kesalahan saat mengirim ke {nomor}: {e}")

# Daftar nomor yang akan dikirim pesan
daftar_nomor = [
    "+6287777777777",
    "+6288888888888",  # Contoh nomor tambahan
]

# Pesan yang ingin dikirim
pesan = "Halo. Selamat Siang"

# Waktu pengiriman awal (sekarang + 1 menit)
waktu_sekarang = datetime.now()
waktu_pengiriman = waktu_sekarang + timedelta(minutes=1)

# Loop untuk mengirim pesan ke setiap nomor
for nomor in daftar_nomor:
    jam_pengiriman = waktu_pengiriman.hour
    menit_pengiriman = waktu_pengiriman.minute
    kirim_pesan(nomor, pesan, jam_pengiriman, menit_pengiriman)
    waktu_pengiriman += timedelta(seconds=20)  # Tambahkan jeda 20 detik untuk setiap pesan
