import numpy as np
import time
import random

from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple


# ================ RANDOM SEED =====================
np.random.seed(61)
random.seed(61)


# ================= KONSTANTA GLOBAL ===================
KATEGORI_PRODUK = ['SAYUR','BUAH','DAGING','IKAN','BAHAN_POKOK']

TIPE_NODE = ['PETANI','DISTRIBUTOR','PASAR','GUDANG']


# =============== DATA CLASS PRODUK ======================
@dataclass
class Produk:
    kode: str
    nama: str
    kategori: str
    harga_satuan: float
    stok: int
    masa_kadaluarsa_hari: int

# ================= DATA CLASS PENGIRIMAN ==================
@dataclass
class Pengiriman:
    pengiriman_id: int
    dari_node: str
    ke_node: str
    kode_produk: str
    jumlah: int
    prioritas: int
    waktu_kirim: float