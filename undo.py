class RiwayatUndo:
    """Riwayat aktivitas petugas untuk fitur Undo (Stack, prinsip LIFO)."""

    def __init__(self):
        self._data = []

    def push(self, waktu, aktivitas):
        """Menyimpan aktivitas baru di puncak stack. O(1) amortized."""
        self._data.append((waktu, aktivitas))

    def pop(self):
        """Membatalkan aktivitas terakhir (mengambil dari puncak). O(1)."""
        if self.is_empty():
            raise IndexError("Tidak ada aktivitas untuk dibatalkan")
        return self._data.pop()

    def peek(self):
        """Melihat aktivitas terakhir tanpa membatalkan. O(1)."""
        if self.is_empty():
            raise IndexError("Tidak ada aktivitas untuk dibatalkan")
        return self._data[-1]

    def is_empty(self):
        """Memeriksa apakah stack kosong. O(1)."""
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def tampil(self):
        """Isi stack dari dasar ke puncak."""
        return [f"{w} | {a}" for w, a in self._data]