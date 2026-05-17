"""
Circular Queue berbasis array (fixed capacity)
Digunakan sebagai buffer stok gudang (FIFO)

Data yang disimpan:
(kode_produk, jumlah, sisa_hari_kadaluarsa)
"""

class CircularQueue:
    def __init__(self, kapasitas: int):
        self.kapasitas = kapasitas
        self.buffer = [None] * kapasitas
        self.front = 0
        self.rear = 0
        self._size = 0

    # =========================
    # OPERASI UTAMA
    # =========================

    def enqueue(self, item):
        """
        Menambah item ke belakang antrian.
        Return False jika buffer penuh.
        Big-O: O(1)
        """
        if self.is_full():
            return False
        
        self.buffer[self.rear] = item
        self.rear = (self.rear + 1) % self.kapasitas
        self._size += 1
        return True

    def dequeue(self):
        """
        Mengambil item paling lama (FIFO).
        Return None jika kosong.
        Big-O: O(1)
        """
        if self.is_empty():
            return None
        
        item = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.kapasitas
        self._size -= 1
        return item

    # =========================
    # HELPER
    # =========================

    def peek(self):
        """Melihat item paling depan tanpa menghapus."""
        if self.is_empty():
            return None
        return self.buffer[self.front]

    def is_full(self):
        return self._size == self.kapasitas

    def is_empty(self):
        return self._size == 0

    def clear(self):
        """Kosongkan buffer."""
        self.front = 0
        self.rear = 0
        self._size = 0
        self.buffer = [None] * self.kapasitas

    def __len__(self):
        return self._size

    # =========================
    # DEBUG / LAPORAN
    # =========================

    def tampilkan_isi(self):
        """Menampilkan isi queue dari depan ke belakang."""
        if self.is_empty():
            print("Buffer kosong")
            return
        
        idx = self.front
        for _ in range(self._size):
            print(self.buffer[idx])
            idx = (idx + 1) % self.kapasitas