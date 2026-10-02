from collections import deque


class AntreanLayanan:
    """Antrean layanan mahasiswa (Queue, prinsip FIFO)."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, nomor_urut, nama):
        """Menambahkan mahasiswa ke belakang antrean. O(1)."""
        self._data.append((nomor_urut, nama))

    def dequeue(self):
        """Melayani (mengambil) mahasiswa paling depan. O(1)."""
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data.popleft()

    def front(self):
        """Melihat mahasiswa paling depan tanpa menghapus. O(1)."""
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data[0]

    def is_empty(self):
        """Memeriksa apakah antrean kosong. O(1)."""
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def tampil(self):
        """Isi antrean dari depan ke belakang."""
        return [f"{no}. {nama}" for no, nama in self._data]