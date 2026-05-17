import pytest
from src.data_structures.circular_queue import CircularQueue
from src.data_models import Produk


def buat_produk(kode):
    return Produk(
        kode=kode,
        nama="Dummy",
        kategori="SAYUR",
        harga_satuan=1000,
        stok=10,
        masa_kadaluarsa_hari=5
    )


# ===============================
# Test enqueue & dequeue dasar
# ===============================
def test_enqueue_dequeue_fifo():
    q = CircularQueue(3)

    p1 = buat_produk("P1")
    p2 = buat_produk("P2")

    assert q.enqueue(p1) == True
    assert q.enqueue(p2) == True

    assert q.dequeue().kode == "P1"
    assert q.dequeue().kode == "P2"


# ===============================
# Test queue kosong
# ===============================
def test_dequeue_empty():
    q = CircularQueue(2)
    assert q.dequeue() is None
    assert q.is_empty() == True


# ===============================
# Test queue penuh
# ===============================
def test_enqueue_full():
    q = CircularQueue(2)

    assert q.enqueue(buat_produk("P1")) == True
    assert q.enqueue(buat_produk("P2")) == True
    assert q.enqueue(buat_produk("P3")) == False  # harus gagal


# ===============================
# Test ukuran queue (__len__)
# ===============================
def test_len_queue():
    q = CircularQueue(5)

    q.enqueue(buat_produk("P1"))
    q.enqueue(buat_produk("P2"))

    assert len(q) == 2

    q.dequeue()
    assert len(q) == 1


# ===============================
# Test circular behaviour
# ===============================
def test_circular_behavior():
    q = CircularQueue(3)

    q.enqueue(buat_produk("P1"))
    q.enqueue(buat_produk("P2"))
    q.enqueue(buat_produk("P3"))

    assert q.dequeue().kode == "P1"
    assert q.dequeue().kode == "P2"

    # rear harus muter ke depan lagi
    assert q.enqueue(buat_produk("P4")) == True
    assert q.enqueue(buat_produk("P5")) == True

    assert q.dequeue().kode == "P3"
    assert q.dequeue().kode == "P4"
    assert q.dequeue().kode == "P5"