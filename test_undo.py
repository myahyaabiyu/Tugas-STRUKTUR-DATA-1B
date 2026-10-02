import unittest
from undo import RiwayatUndo


class TestRiwayatUndo(unittest.TestCase):
    def setUp(self):
        self.s = RiwayatUndo()

    def test_push(self):
        self.s.push("08:00", "Input KRS")
        self.s.push("08:10", "Cetak surat")
        self.assertEqual(self.s.size(), 2)
        self.assertEqual(self.s.peek(), ("08:10", "Cetak surat"))

    def test_pop_lifo(self):
        self.s.push("08:00", "A1")
        self.s.push("08:10", "A2")
        self.s.push("08:20", "A3")
        self.assertEqual(self.s.pop(), ("08:20", "A3"))
        self.assertEqual(self.s.pop(), ("08:10", "A2"))
        self.assertEqual(self.s.size(), 1)

    def test_pop_kosong(self):
        with self.assertRaises(IndexError):
            self.s.pop()

    def test_peek(self):
        self.s.push("08:00", "A1")
        self.s.push("08:10", "A2")
        self.assertEqual(self.s.peek(), ("08:10", "A2"))
        self.assertEqual(self.s.size(), 2)

    def test_peek_kosong(self):
        with self.assertRaises(IndexError):
            self.s.peek()

    def test_is_empty(self):
        self.assertTrue(self.s.is_empty())
        self.s.push("08:00", "A1")
        self.assertFalse(self.s.is_empty())
        self.s.pop()
        self.assertTrue(self.s.is_empty())


if __name__ == "__main__":
    unittest.main()