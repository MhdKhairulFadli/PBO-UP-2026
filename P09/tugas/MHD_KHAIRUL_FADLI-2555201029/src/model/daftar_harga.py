
"""Daftar harga untuk berbagai objek yang dapat disewakan."""

from src.model.sewaan import Sewaan


class DaftarHarga:
    """Mengelola objek sewaan berdasarkan kontrak Sewaan."""

    def __init__(self, alat: list[Sewaan]) -> None:
        if not alat:
            raise ValueError("daftar sewaan tidak boleh kosong")

        self._alat = list(alat)

    def biaya_semua(self, jumlah_hari: int) -> list[int]:
        """Menghitung biaya setiap objek sewaan."""
        return [
            item.biaya_sewa(jumlah_hari)
            for item in self._alat
        ]

    def termurah(self, jumlah_hari: int) -> Sewaan:
        """Mengembalikan objek dengan biaya sewa termurah."""
        return min(
            self._alat,
            key=lambda item: item.biaya_sewa(jumlah_hari),
        )

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        """Menghitung total biaya jika semua objek disewa."""
        return sum(self.biaya_semua(jumlah_hari))
