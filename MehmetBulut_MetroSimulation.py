from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

# 🚉 Metro istasyonlarını temsil eden sınıf
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx # İstasyon ID'si
        self.ad = ad   # İstasyon adı
        self.hat = hat # Hangi metro hattına ait olduğu
        self.komsular: List[Tuple['Istasyon', int]] = [] #(komşu istasyon, süre)

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        """Bir istasyonu komşu olarak ekler"""
        self.komsular.append((istasyon, sure))

    def __lt__(self, other: 'Istasyon'):
        """A* algoritmasında öncelik kuyruğu için kıyaslama"""
        return self.idx < other.idx

# 🚇 Metro ağını temsil eden sınıf
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}  # İstasyon ID -> İstasyon nesnesi
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list) # Hat adı -> İstasyon Listesi

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        """Yeni bir istasyon ekler"""
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        """İki istasyon arasında bağlantı kurar"""
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    # 🔎 En az aktarmalı rota (BFS)
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS kullanarak en az aktarmalı rotayı bulur"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        kuyruk = deque([(baslangic, [baslangic])]) #(mevcut istasyon , yol)
        ziyaret_edildi = set()

        while kuyruk:
            mevcut, yol = kuyruk.popleft()

            if mevcut == hedef:
                return yol #En az aktarmalı yolu buluyoruz

            ziyaret_edildi.add(mevcut)

            for komsu, _ in mevcut.komsular:
                if komsu not in ziyaret_edildi:
                    kuyruk.append((komsu, yol + [komsu]))

        return None  # Yol bulunamadı

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = [(0, baslangic, [baslangic])] #(toplam süre, mevcut istasyon, yol)
        ziyaret_edildi = set()

        while pq:
            sure, mevcut, yol = heapq.heappop(pq)

            if mevcut == hedef:
                return yol, sure #En hızlı yolu buluyoruz

            ziyaret_edildi.add(mevcut)

            for komsu, gecis_suresi in mevcut.komsular:
                if komsu not in ziyaret_edildi:
                    heapq.heappush(pq, (sure + gecis_suresi, komsu, yol + [komsu]))

        return None #Yol bulunamadı


# 🚀 Metro sistemini oluştur
if __name__ == "__main__":
    metro = MetroAgi()

    # 🔴 Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # 🔵 Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # 🟠 Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantıları ekle
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)

    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)

    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)

    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)

    # 📝 Test Senaryoları
    testler = [
        ("M1", "K4"),
        ("T1", "T4"),
        ("T4", "M1"),
        ("K2", "T4"),
        ("M3", "K4"),
        ("M1", "T1"),
        ("M4", "K1"),
        ("T4", "K4"),
    ]

    for idx, (baslangic, hedef) in enumerate(testler, start=1):
        print(f"\n🚀 **{idx}. {metro.istasyonlar[baslangic].ad} → {metro.istasyonlar[hedef].ad}**:")

        rota = metro.en_az_aktarma_bul(baslangic, hedef)
        if rota:
            print(f"📌 **En az aktarmalı rota**: 🚉 {' ➝ '.join(i.ad for i in rota)}")

        sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
        if sonuc:
            rota, sure = sonuc
            print(f"⚡ **En hızlı rota** ({sure} dk): 🚀 {' ➝ '.join(i.ad for i in rota)}")
