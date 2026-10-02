import unittest
from antrean import AntreanLayanan


class TestAntreanLayanan(unittest.TestCase):
    def setUp(self):
        self.q = AntreanLayanan()

    def test_enqueue(self):
        self.q.enqueue(1, "Andi")
        self.q.enqueue(2, "Siti")
        self.assertEqual(self.q.size(), 2)
        self.assertEqual(self.q.tampil(), ["1. Andi", "2. Siti"])

    def test_dequeue_fifo(self):
        for i, n in enumerate(["Andi", "Siti", "Budi"], start=1):
            self.q.enqueue(i, n)
        self.assertEqual(self.q.dequeue(), (1, "Andi"))
        self.assertEqual(self.q.dequeue(), (2, "Siti"))
        self.assertEqual(self.q.size(), 1)

    def test_dequeue_kosong(self):
        with self.assertRaises(IndexError):
            self.q.dequeue()

    def test_front(self):
        self.q.enqueue(1, "Andi")
        self.q.enqueue(2, "Siti")
        self.assertEqual(self.q.front(), (1, "Andi"))
        self.assertEqual(self.q.size(), 2)

    def test_front_kosong(self):
        with self.assertRaises(IndexError):
            self.q.front()

    def test_is_empty(self):
        self.assertTrue(self.q.is_empty())
        self.q.enqueue(1, "Andi")
        self.assertFalse(self.q.is_empty())
        self.q.dequeue()
        self.assertTrue(self.q.is_empty())


if __name__ == "__main__":
    unittest.main()