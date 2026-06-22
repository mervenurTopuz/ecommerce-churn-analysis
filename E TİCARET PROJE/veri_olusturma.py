import pandas as pd
import numpy as np

# Her çalıştırmada aynı rastgele verilerin üretilmesi için sabitliyoruz
np.random.seed(42)
n_samples = 1000

# Sentetik E-Ticaret Müşteri Verisi Tasarımı
data = {
    'Musteri_ID': range(1001, 1001 + n_samples),
    'Yas': np.random.randint(18, 65, size=n_samples),
    'Cinsiyet': np.random.choice(['Kadin', 'Erkek'], size=n_samples),
    'Uyelik_Suresi_Ay': np.random.randint(1, 60, size=n_samples),
    'Toplam_Harcama_TL': np.round(np.random.uniform(500, 25000, size=n_samples), 2),
    'Son_Alisveristen_Gecen_Gun': np.random.randint(1, 120, size=n_samples),
    'Destek_Talebi_Sayisi': np.random.randint(0, 8, size=n_samples),
    'Sepette_Urun_Birakma_Sayisi': np.random.randint(0, 6, size=n_samples),
    # Churn: 1 (Terk etti), 0 (Aktif müşteri) -> Dağılımı %75 aktif, %25 terk şeklinde kurgulayalım
    'Churn': np.random.choice([0, 1], size=n_samples, p=[0.75, 0.25])
}

# Veriyi DataFrame yapısına dönüştürelim
df = pd.DataFrame(data)

# Veriyi daha sonra kullanmak üzere bilgisayara CSV olarak kaydedelim
df.to_csv('ecommerce_churn_data.csv', index=False)

# Oluşturduğumuz tablonun ilk 5 satırına göz atalım
print("--- Veri Setinin İlk 5 Satırı ---")
print(df.head())

# Sütunların veri tiplerini ve boş (null) değer olup olmadığını kontrol edelim
print("\n--- Veri Seti Genel Bilgileri ---")
print(df.info())
