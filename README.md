# Shopee Affiliate Automation & Threads Content Engine 🧵✨

Sistem otomatisasi pembuatan konten dan manajemen produk **Shopee Affiliate Program** yang dioptimalkan khusus untuk platform **Meta Threads**.

---

## 🎯 Mengapa Meta Threads?
- **Algoritma Terbuka**: Postingan akun baru langsung disalurkan ke linimasa publik (*For You* feed).
- **Gaya Bercerita (Storytelling)**: Pembaca menyukai curhat hemat, rekomendasi barang terjangkau, dan *honest review*.
- **Konversi Anti-Shadowban**: Formula pemisahan antara **Postingan Utama** (cerita + gambar) dan **Balasan Pertama** (link affiliate Shopee).

---

## 📁 Struktur Repositori
```text
├── .github/
│   └── workflows/
│       └── scheduled_reminder.yml  # Otomatisasi jadwal di GitHub Actions
├── scripts/
│   └── format_threads_copy.py      # Generator template copywriting Threads
├── database/
│   └── affiliate_links.json        # Arsip lokal link produk & status
├── requirements.txt
└── README.md
```

---

## 🚀 Alur Kerja Sistem (Workflow)
1. **Input Link Shopee**: Salin tautan produk dari Shopee Affiliate (tab Komisi XTRA).
2. **AI Processing**: AI menyusun 3 varian naskah (Curhat Hemat, Unpopular Opinion, Rekomendasi Solutif).
3. **Sinkronisasi**: Tersinkronisasi dengan [Google Spreadsheet Pelacakan](https://docs.google.com/spreadsheets/d/1rEtHanEwU0NNDZRwIg6lwPo7SBPvjO2vf8CgD-tyghU/edit).
4. **Distribusi**: Unggah ke Meta Threads di jam sibuk audiens (07:00–09:00 atau 19:00–21:00).
