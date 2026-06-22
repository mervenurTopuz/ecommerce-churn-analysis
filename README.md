# ecommerce-churn-analysis
# 🛒 E-Ticaret Müşteri Terk (Churn) Analizi ve Modellemesi

Bu proje, bir e-ticaret platformundaki müşteri davranışlarını analiz ederek, platformu terk etme (churn) riski taşıyan müşterileri makine öğrenmesi teknikleriyle önceden tespit etmeyi amaçlamaktadır. Projede veri madenciliği süreçleri uçtan uca uygulanmıştır.

## 📌 Proje Amacı
Müşteri kazanım maliyetlerinin (CAC) arttığı günümüzde, mevcut müşteriyi elde tutmak stratejik bir öneme sahiptir. Bu proje ile:
* Sentetik e-ticaret verileri üzerinden müşteri demografisi ve satın alma geçmişi (RFM metrikleri) incelenmiş,
* Karar Ağacı (Decision Tree) algoritması kurularak risk tahmini yapılmış,
* Sınıf dengesizliği (Imbalanced Data) problemi çözülerek modelin riskli müşterileri gözden kaçırması engellenmiştir.

## 🛠️ Kullanılan Teknolojiler
* **Programlama Dili:** Python
* **Veri Manipülasyonu:** Pandas, NumPy
* **Makine Öğrenmesi:** Scikit-Learn
* **Veri Görselleştirme:** Matplotlib, Seaborn

## 🚀 Model Performansı ve İş Zekası (BI) Yaklaşımı

Modelin ilk sürümünde genel Doğruluk (Accuracy) %77 seviyelerinde görünmesine rağmen, terk eden müşterileri yakalama oranı (Recall) %0'dı. Veri setindeki dengesizlik (aktif müşterilerin çoğunlukta olması) algoritmayı yanıltıyordu.

Gerçek dünya iş problemlerinde (özellikle Churn analizinde) asıl maliyet, ayrılacak müşteriyi gözden kaçırmaktır. Bu nedenle modele `class_weight='balanced'` parametresi eklenerek algoritmik bir optimizasyon yapılmış ve **Terk Eden Müşterileri Yakalama Oranı (Recall) %83'e** çıkartılmıştır. 

* **Genel Doğruluk (Accuracy):** %35.00
* **Terk Eden Sınıfı Duyarlılığı (Recall - Sınıf 1):** %83

**Analitik Yorum:** Rastgele üretilen sentetik veriler üzerinde çalışıldığı için model ayrılacak kişileri yakalamak adına agresif davranmış ve genel doğruluk oranını düşürmüştür. Ancak iş birimlerinin (Pazarlama ve CRM) kayıp riski taşıyan kitleye yönelik aksiyon alabilmesi için en kritik metrik olan duyarlılık (Recall) başarıyla maksimize edilmiştir.

## 📂 Proje Adımları
1. **Veri Üretimi (`veri_olusturma.py`):** 1000 satırlık demografik ve davranışsal e-ticaret metriklerini içeren veri seti tasarlandı.
2. **Keşifsel Veri Analizi (`gorsellestirme.py`):** Yaş, cinsiyet ve harcama alışkanlıklarının churn üzerindeki etkisi görselleştirildi.
3. **Makine Öğrenmesi (`model_kurulumu.py`):** Entropi kriteri kullanılarak Karar Ağacı eğitildi ve sınıflandırma raporları oluşturuldu.
