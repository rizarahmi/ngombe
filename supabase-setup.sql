-- Kasir ngoombé: tabel + keamanan (RLS). Jalankan sekali di Supabase > SQL Editor.
-- Aman dijalankan ulang.

create table if not exists public.app_settings (
  id         int primary key default 1 check (id = 1),
  data       jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

create table if not exists public.transactions (
  id         text primary key,
  ts         bigint not null,
  data       jsonb not null,
  created_at timestamptz not null default now()
);
create index if not exists transactions_ts_idx on public.transactions (ts);

-- Owner = akun aderiza@ngoombe.app
create or replace function public.is_owner() returns boolean
language sql stable as $$
  select lower(coalesce(auth.jwt() ->> 'email', '')) = 'aderiza@ngoombe.app'
$$;

alter table public.app_settings enable row level security;
alter table public.transactions enable row level security;

drop policy if exists "baca pengaturan"   on public.app_settings;
drop policy if exists "tulis pengaturan"  on public.app_settings;
drop policy if exists "ubah pengaturan"   on public.app_settings;
drop policy if exists "baca transaksi"    on public.transactions;
drop policy if exists "tambah transaksi"  on public.transactions;
drop policy if exists "hapus transaksi"   on public.transactions;

-- Semua yang login boleh membaca; hanya owner boleh mengubah pengaturan & menghapus transaksi
create policy "baca pengaturan"  on public.app_settings for select to authenticated using (true);
create policy "tulis pengaturan" on public.app_settings for insert to authenticated with check (public.is_owner());
create policy "ubah pengaturan"  on public.app_settings for update to authenticated using (public.is_owner()) with check (public.is_owner());

create policy "baca transaksi"   on public.transactions for select to authenticated using (true);
create policy "tambah transaksi" on public.transactions for insert to authenticated with check (true);
create policy "hapus transaksi"  on public.transactions for delete to authenticated using (public.is_owner());

-- Realtime: perangkat lain langsung update saat ada perubahan
do $$ begin
  alter publication supabase_realtime add table public.transactions;
exception when duplicate_object then null; end $$;
do $$ begin
  alter publication supabase_realtime add table public.app_settings;
exception when duplicate_object then null; end $$;
