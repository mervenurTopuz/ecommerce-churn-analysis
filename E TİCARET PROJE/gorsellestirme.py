import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Oluşturduğumuz veriyi okuyoruz
df = pd.read_csv('ecommerce_churn_data.csv')

print("Veri başarıyla yüklendi. Grafikler hazırlanıyor...\n")
print("Lütfen açılan grafik penceresini inceledikten sonra kapatın.")
print("Bir pencereyi kapatmadan diğer grafik açılmaz!\n")

# Grafiklerin genel tasarım temasını ayarlayalım
sns.set_theme(style="whitegrid")

# 2. Genel Churn (Terk) Dağılımı Grafiği
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Churn', palette='Set2')
plt.title('Genel Müşteri Terk (Churn) Dağılımı\n(0: Aktif, 1: Terk)')
plt.ylabel('Müşteri Sayısı')
plt.show()

# 3. Cinsiyete Göre Churn Grafiği
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Cinsiyet', hue='Churn', palette='Pastel1')
plt.title('Cinsiyete Göre Müşteri Terk Durumu')
plt.ylabel('Müşteri Sayısı')
plt.show()

# 4. Yaş ve Harcama Dağılımı (Kutu Grafiği - Boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Churn', y='Toplam_Harcama_TL', palette='Set3')
plt.title('Terk Eden vs Aktif Müşterilerin Harcama Dağılımı')
plt.xlabel('0: Aktif | 1: Terk')
plt.ylabel('Harcama Tutarı (TL)')
plt.show()

print("Tüm grafikler başarıyla çizdirildi! Analiz aşaması tamamlandı.")
