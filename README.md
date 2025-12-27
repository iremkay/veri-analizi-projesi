# � Nesli Tükenen Hayvanlar Veri Analizi

Bu proje, **Streamlit tabanlı bir veri analizi uygulamasıdır** ve dünya üzerindeki **nesli tükenme tehlikesi altında olan hayvanları** inceler.

Uygulama, koruma statüleri, popülasyon verileri, tehdit seviyeleri ve habitat bilgileri üzerinden kapsamlı analizler sunar.

---

## 🌍 Veri Seti Hakkında

Veri seti **45 farklı nesli tükenmekte olan hayvan türü** içermektedir:

### Özellikler:
- **animal_name:** Hayvan adı
- **scientific_name:** Bilimsel adı
- **conservation_status:** Koruma statüsü (Critically Endangered, Endangered, Vulnerable)
- **population:** Tahmini popülasyon
- **habitat:** Yaşam alanı
- **continent:** Kıta
- **threat_level:** Tehdit seviyesi (1-10)
- **body_weight_kg:** Ortalama vücut ağırlığı (kg)
- **lifespan_years:** Ortalama yaşam süresi (yıl)
- **diet_type:** Beslenme türü

---

## ✨ Özellikler

Uygulama aşağıdaki adımları içerir:

### 1. **Veri Seti Genel Bakış**
   - Veri seti boyutu (satır & sütun sayısı)
   - Sütun isimleri

### 2. **Ham Veri Önizleme**
   - İnteraktif satır seçimi
   - Tablo görselleştirmesi

### 3. **İstatistiksel Özetler**
   - `df.describe(include="all")` kullanılarak tam özet
   - **Sayısal ve kategorik** özellikleri kapsar

### 4. **Veri Tipi İncelemesi**
   - Sütun bazında veri tipi listesi

### 5. **Eksik Değer Analizi**
   - Sütun başına eksik değer sayıları
   - Eksik değer görselleştirmesi

### 6. **Sayısal Özellik Tespiti**
   - Sayısal özelliklerin otomatik tespiti

### 7. **Korelasyon Analizi**
   - Pearson korelasyon matrisi
   - Seaborn kullanarak ısı haritası görselleştirmesi

### 8. **Standartlaştırma**
   - Sayısal özelliklere Z-skoru normalizasyonu uygulanır
   - Standartlaştırılmış veri seti önizlemesi

### 9. **Temel Bileşen Analizi (PCA)**
   - Standartlaştırılmış sayısal özellikler üzerinde PCA uygulanır
   - İlk iki temel bileşen (PC1 & PC2)
   - Açıklanan varyans oranı
   - 2D dağılım grafiği görselleştirmesi

### 10. **Kutu Grafikleri (Box Plots)**
   - Aykırı değer (outlier) tespiti
   - Veri dağılımı görselleştirmesi

---

## 🚀 Kurulum

### Gereksinimler

Python 3.8 veya üzeri versiyonun yüklü olması gerekmektedir.

### Adımlar

1. **Repoyu klonlayın:**
   ```bash
   git clone https://github.com/iremkay/veri-analizi-projesi.git
   cd veri-analizi-projesi
   ```

2. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı çalıştırın:**
   ```bash
   streamlit run app.py
   ```

4. **Tarayıcıda açın:**
   Uygulama otomatik olarak tarayıcınızda `http://localhost:8501` adresinde açılacaktır.

---

## 📁 Proje Yapısı

```
veri-analizi-projesi/
│
├── app.py                      # Ana Streamlit uygulaması
├── requirements.txt            # Python bağımlılıkları
├── endangered_animals.csv      # Nesli tükenen hayvanlar veri seti
└── README.md                   # Proje dokümantasyonu
```

---

## 🎯 Kullanım

1. Uygulamayı çalıştırın
2. Veri seti otomatik olarak yüklenir
3. Otomatik olarak gerçekleştirilen analizleri inceleyin:
   - Koruma statüsü dağılımı
   - Popülasyon istatistikleri
   - Tehdit seviyesi analizleri
   - Habitat ve kıta dağılımları
   - Korelasyon analizi
   - PCA sonuçları

---

## 📊 Örnek Veri Seti

Proje, **45 nesli tükenmekte olan hayvan türünü** içeren gerçek verilere dayalı bir veri seti kullanmaktadır:
- **Critically Endangered** (Kritik Derecede Tehlike Altında): Amur Leopard, Javan Rhino, Vaquita
- **Endangered** (Tehlike Altında): Mountain Gorilla, Bengal Tiger, Red Panda  
- **Vulnerable** (Hassas): Giant Panda, Polar Bear, Snow Leopard

---

## 🛠️ Kullanılan Teknolojiler

- **Streamlit** - Web uygulaması framework'ü
- **Pandas** - Veri manipülasyonu
- **Matplotlib & Seaborn** - Veri görselleştirme
- **Scikit-learn** - Makine öğrenmesi algoritmaları (StandardScaler, PCA)

---

## 📝 Notlar

- Veri seti otomatik olarak GitHub'dan yüklenir
- Sidebar'dan farklı veri setleri de yüklenebilir
- Tüm analizler interaktif ve gerçek zamanlıdır

---

## 📧 İletişim

Sorularınız veya geri bildirimleriniz için lütfen iletişime geçin.

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.
