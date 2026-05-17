from src.data_models import Produk


class CircularQueue:
    """
    Circular Queue berbasis array (fixed capacity).
    FIFO = produk pertama masuk, pertama keluar.
    """

    def __init__(self, kapasitas: int):
        self.kapasitas = kapasitas
        self.buffer = [None] * kapasitas
        self.front = 0
        self.rear = 0
        self._size = 0

    # enqueue O(1)
    def enqueue(self, produk: Produk):
        """Kembalikan False jika penuh"""
        if self.is_full():
            return False

        self.buffer[self.rear] = produk
        self.rear = (self.rear + 1) % self.kapasitas
        self._size += 1
        return True

    # dequeue O(1)
    def dequeue(self):
        """Ambil produk terlama (FIFO)"""
        if self.is_empty():
            return None

        produk = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.kapasitas
        self._size -= 1
        return produk

    def is_full(self):
        return self._size == self.kapasitas

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size