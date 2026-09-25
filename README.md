# ngombe

Aplikasi kasir sederhana berbasis web (satu file `index.html`), tanpa server.

## Fitur
- Kasir: pilih menu, atur jumlah, bayar Tunai / QRIS / Transfer, hitung kembalian, cetak struk.
- Pengaturan daftar menu & harga (bisa diaktifkan/nonaktifkan).
- Pembagian alokasi pendapatan per menu, dalam % atau nominal Rp.
- Riwayat transaksi per tanggal.
- Laporan omzet + total per pos alokasi, ekspor CSV.
- Cadangan & pulihkan data (file JSON).

## Deploy ke GitHub Pages
1. Buat repository baru di GitHub (misal `kasir-smoothie`), boleh Public.
2. Upload `index.html` (dan README ini) lewat **Add file → Upload files**, lalu **Commit**.
3. Buka **Settings → Pages**. Di *Source* pilih **Deploy from a branch**, branch `main`, folder `/ (root)`, klik **Save**.
4. Tunggu 1–2 menit, aplikasi bisa dibuka di `https://USERNAME.github.io/kasir-smoothie/`.

Untuk update: edit/upload ulang `index.html` di repo, GitHub Pages akan memperbarui otomatis.

## Penting soal data
Data (menu, transaksi) disimpan di browser perangkat yang dipakai (localStorage), bukan di GitHub.
- Pakai satu perangkat/browser yang sama untuk kasir.
- Jangan "Clear browsing data" di browser tersebut.
- Rutin klik **Pengaturan → Unduh cadangan**.
