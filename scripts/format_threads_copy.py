#!/usr/bin/env python3
"""
Threads Copywriting Formatter & Template Generator
Membantu memformat draft postingan Threads sesuai formula konversi tinggi.
"""

def generate_threads_draft(store_name: str, category: str, affiliate_url: str, voucher_info: str = "Diskon s.d 50rb"):
    print("=" * 60)
    print(f"🧵 GENERATING THREADS DRAFT: {store_name}")
    print("=" * 60)
    
    post_main = f"""Jujur, semenjak kerja/kuliah udah ga pernah lagi gengsi beli sneakers jutaan cuma buat daily walk atau tempur di jalanan.

Asal solnya empuk, modelnya ga norak, dan harganya under 150rb udah lebih dari cukup. Kemarin nemu toko lokal {store_name} ini pas lagi iseng nyari sepatu santai, ternyata banyak model Korean style yang estetik bgt dan ga gampang jebol.

Daripada boncos tiap bulan beli sepatu mahal cuma buat harian, toko ini penyelamat dompet bgt sih 😭

(Sertakan 1-2 foto sepatu terestetik dari toko ini)"""

    reply_first = f"""Buat yang nanya nama tokonya atau mau cek model lainnya, link katalog resminya di sini yaa (lagi ada {voucher_info}):
👉 {affiliate_url}"""

    print("\n[1] POSTINGAN UTAMA (Tanpa link keluar):")
    print("-" * 40)
    print(post_main)
    print("\n[2] BALASAN PERTAMA (Komentar sendiri berisi link):")
    print("-" * 40)
    print(reply_first)
    print("=" * 60)

if __name__ == "__main__":
    generate_threads_draft(
        store_name="Lucky Fan Store",
        category="Sepatu Sneakers & Sandal Pria/Wanita",
        affiliate_url="https://s.shopee.co.id/3B8qMvggvL"
    )
