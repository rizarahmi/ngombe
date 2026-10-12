# Kasir ngoombé

Aplikasi kasir berbasis web (`index.html`), di-host gratis di GitHub Pages.
Data disimpan di database online **Supabase**, jadi sama di semua perangkat.

## Setup Supabase (sekali saja)
1. Daftar di https://supabase.com lalu buat **New project** (nama: `ngoombe`, region: Southeast Asia/Singapore).
2. **SQL Editor → New query**, tempel isi `supabase-setup.sql`, klik **Run**.
3. **Authentication → Users → Add user → Create new user** (centang *Auto Confirm User*):
   - `aderiza@ngoombe.app` / password owner
   - `ngoombe@ngoombe.app` / password karyawan
   Di aplikasi, login tetap pakai username `aderiza` atau `ngoombe`.
4. **Authentication → Sign In / Providers**: matikan **Allow new users to sign up**.
5. **Project Settings → API Keys / Data API**: salin **Project URL** dan **anon public / publishable key**,
   lalu isi di `index.html` bagian `SUPABASE_URL` dan `SUPABASE_KEY`.
   Jangan pernah memakai kunci `service_role` / `secret` di aplikasi.

Kalau `SUPABASE_URL` dikosongkan, aplikasi berjalan dalam mode lokal (data hanya di perangkat itu).

## Deploy / update
Upload `index.html` ke repo lalu Commit. GitHub Pages memperbarui otomatis dan aplikasi yang
sedang terbuka akan memuat versi baru sendiri.

## Offline
Kalau internet putus, transaksi tetap tersimpan di perangkat dan otomatis terkirim begitu online.
Status sinkron terlihat di pojok kanan atas.
