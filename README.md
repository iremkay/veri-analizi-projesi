# 📊 Keşifsel Veri Analizi (EDA) Streamlit Uygulaması

Bu proje, **Streamlit tabanlı bir Keşifsel Veri Analizi (EDA) uygulamasıdır** ve **Veri Bilimi ve Makine Öğrenmesi** dersleri için eğitim amaçlı tasarlanmıştır.

Uygulama, ham veri incelemesinden korelasyon analizi, standartlaştırma ve **Temel Bileşen Analizi (PCA)** gibi işlemlere kadar kapsamlı bir yol haritası sunar.

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

1. **Repoyu klonlayın veya dosyaları indirin:**
   ```bash
   git clone <repo-url>
   cd proje.streamlit
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
proje.streamlit/
│
├── app.py                 # Ana Streamlit uygulaması
├── requirements.txt       # Python bağımlılıkları
├── ornek_veri.csv        # Örnek veri seti (test için)
└── README.md             # Proje dokümantasyonu
```

---

## 🎯 Kullanım

1. Uygulamayı çalıştırın
2. **CSV dosyanızı yükleyin** (veya `ornek_veri.csv` dosyasını kullanın)
3. Otomatik olarak gerçekleştirilen analizleri inceleyin:
   - Veri seti özeti
   - İstatistiksel bilgiler
   - Görselleştirmeler
   - Korelasyon analizi
   - PCA sonuçları

---

## 📊 Örnek Veri Seti

Proje, test amaçlı bir örnek veri seti (`ornek_veri.csv`) içermektedir:
- **30 satır** çalışan verisi
- **7 sütun:** isim, yaş, şehir, maaş, deneyim yılı, eğitim seviyesi, performans skoru
- Hem sayısal hem de kategorik özellikler

---

## 🛠️ Kullanılan Teknolojiler

- **Streamlit** - Web uygulaması framework'ü
- **Pandas** - Veri manipülasyonu
- **Matplotlib & Seaborn** - Veri görselleştirme
- **Scikit-learn** - Makine öğrenmesi algoritmaları (StandardScaler, PCA)

---

## 📝 Notlar

- CSV dosyanız **ilk satırda sütun başlıkları** içermelidir
- Veriler **virgül (,)** ile ayrılmalıdır
- Hem sayısal hem de kategorik veriler desteklenir
- Büyük veri setleri için önizleme satır sayısını ayarlayabilirsiniz

---

## 📧 İletişim

Sorularınız veya geri bildirimleriniz için lütfen iletişime geçin.

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir ve serbestçe kullanılabilir.
