from antrean import AntreanLayanan
from undo import RiwayatUndo


def simulasi_antrean():
    print("= SIMULASI ANTREAN LAYANAN MAHASISWA (QUEUE) =")
    q = AntreanLayanan()
    print("Awal            :", q.tampil(), "| kosong:", q.is_empty())

    q.enqueue(1, "Yahya Abiyu")
    print("1. Enqueue Abiyu :", q.tampil())
    q.enqueue(2, "Nabila Shifa")
    print("2. Enqueue Nabila :", q.tampil())
    q.enqueue(3, "Moza Mafifa")
    print("3. Enqueue Moza :", q.tampil())
    print("4. Front        :", q.front(), "->", q.tampil())
    print("5. Dequeue      :", q.dequeue(), "->", q.tampil())
    q.enqueue(4, "Tiara Pratiwi")
    print("6. Enqueue Tiara :", q.tampil())
    q.enqueue(5, "Jespri Gustian")
    print("7. Enqueue Jespri:", q.tampil())
    print("8. Is empty     :", q.is_empty())
    print("Hasil akhir     :", q.tampil(), "| depan:", q.front())


def simulasi_undo():
    print("\n=== SIMULASI FITUR UNDO (STACK) ===")
    s = RiwayatUndo()
    data = [
        ("2026-10-03 08:00", "Input berkas KRS Yahya Abiyu"),
        ("2026-10-03 08:10", "Cetak surat keterangan aktif Nabila Shifa"),
        ("2026-10-03 08:20", "Verifikasi data Moza Mafifa"),
        ("2026-10-03 08:30", "Ubah alamat Tiara Pratiwi"),
        ("2026-10-03 08:40", "Legalisir transkrip Jespri Gustian"),
    ]
    for i, (w, a) in enumerate(data, start=1):
        s.push(w, a)
        print(f"{i}. Push A{i}    :", s.size(), "aktivitas, puncak =", s.peek()[1])
    print("6. Peek         :", s.peek())
    print("7. Pop (Undo)   :", s.pop())
    print("   Isi stack    :", s.tampil())
    print("8. Is empty     :", s.is_empty())
    print("Hasil akhir     :", s.tampil(), "| puncak:", s.peek())


if __name__ == "__main__":
    simulasi_antrean()
    simulasi_undo()