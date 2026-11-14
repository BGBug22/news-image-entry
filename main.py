"""news-image-01: tulis satu gambar berita dunia 13 November 2026.

Program ini menyalin news.png yang disertakan (ilustrasi editorial:
perundingan damai Ukraina, kapal tanker di Selat Hormuz, chip, globe)
ke /output/entry.png secara deterministik, hanya dengan stdlib.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")
DST = "/output/entry.png"
MAX_BYTES = 1024 * 1024

os.makedirs("/output", exist_ok=True)
if os.path.exists(DST):
    os.remove(DST)
shutil.copyfile(SRC, DST)
assert os.path.getsize(DST) == os.path.getsize(SRC), "ukuran hasil != sumber"
assert os.path.getsize(DST) < MAX_BYTES, "hasil >= 1 MiB"
