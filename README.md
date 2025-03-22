# 🚇 Sürücüsüz Metro Simülasyonu

Bu proje, bir şehir metrosu için en az aktarma ve en hızlı rotayı hesaplayan bir algoritma içermektedir. **BFS (Breadth-First Search) ve A* (A-Star) algoritmaları kullanılmıştır.**  

---

## 📌 Kullanılan Teknolojiler & Kütüphaneler

| Teknoloji / Kütüphane | Açıklama |
|-----------------------|----------|
| **Python** | Projede kullanılan programlama dili |
| **collections.deque** | BFS algoritması için kuyruk veri yapısı sağlar |
| **heapq** | A* algoritması için öncelik kuyruğu (min-heap) sağlar |
| **defaultdict** | Hat bağlantılarını saklamak için kullanılır |

---

## 📌 Algoritmaların Çalışma Mantığı

### 🔹 **BFS (En Az Aktarma) Algoritması**
**Breadth-First Search (BFS)**, **katmanlı (level-wise) arama yaparak** en kısa yolu bulur.  
Bu projede, **en az aktarma gerektiren metro rotasını** bulmak için BFS kullanılmıştır.

🔹 **Adımlar:**
1. **Kuyruğa başlangıç istasyonunu ekle**  
2. **Ziyaret edilen istasyonları takip et**  
3. **Her adımda komşu istasyonları kuyruğa ekle**  
4. **Hedef istasyona ulaşıldığında dur**  

---

### 🔹 **A* (En Hızlı Rota) Algoritması**
A* algoritması, **g** (şu ana kadar geçen süre) ve **h** (tahmini kalan süre) değerlerini kullanarak **en hızlı rotayı bulur.**  

🔹 **Adımlar:**
1. **Öncelik kuyruğuna (heapq) başlangıç istasyonunu ekle**  
2. **Her istasyon için en kısa süreyi hesapla**  
3. **Ziyaret edilen istasyonları takip et**  
4. **Hedef istasyona ulaşıldığında toplam süreyi döndür**  

---

## 📌 Örnek Kullanım ve Test Sonuçları  

🚀 **Örnek 1: AŞTİ’den OSB’ye Gitmek**  

| Algoritma | Rota | Süre |
|-----------|------|------|
| **BFS** (En az aktarma) | AŞTİ ➝ Kızılay ➝ Ulus ➝ Demetevler ➝ OSB | - |
| **A*** (En hızlı rota) | AŞTİ ➝ Kızılay ➝ Ulus ➝ Demetevler ➝ OSB | **17 dakika** |

🚀 **Örnek 2: Batıkent’ten Keçiören’e Gitmek**  

| Algoritma | Rota | Süre |
|-----------|------|------|
| **BFS** (En az aktarma) | Batıkent ➝ Demetevler ➝ Gar ➝ Keçiören | - |
| **A*** (En hızlı rota) | Batıkent ➝ Demetevler ➝ Gar ➝ Keçiören | **14 dakika** |

---

## 📌 Projeyi Geliştirme Fikirleri 🚀  

Bu projeyi daha da geliştirmek için:  
✅ **Canlı bir kullanıcı arayüzü (GUI) ekleyebiliriz**  
✅ **Gerçek zamanlı metro saatleri ve yoğunluk verisi ekleyebiliriz**  
✅ **Farklı metro ağları için desteği artırabiliriz**  

---
## 📌 Çıktı
![Ekran görüntüsü 2025-03-22 144539](https://github.com/user-attachments/assets/33edc661-6e57-4d0a-bdc1-be96da0566f2)
