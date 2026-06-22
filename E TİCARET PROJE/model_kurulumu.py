import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Veriyi okuma
df = pd.read_csv('ecommerce_churn_data.csv')

# 2. Veri Ön İşleme (Data Preprocessing)
le = LabelEncoder()
df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])

X = df.drop(['Musteri_ID', 'Churn'], axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model Kurulumu ve Eğitimi (Dengeli Sürüm)
# Burada 'balanced' ayarını ekledik ki ayrılacak müşterileri kaçırmasın!
model = DecisionTreeClassifier(criterion='entropy', max_depth=5, class_weight='balanced', random_state=42)

# Hatanın sebebi bu satırın silinmiş olmasıydı, şimdi geri geldi :)
model.fit(X_train, y_train) 

# 4. Tahmin ve Performans Ölçümü
y_pred = model.predict(X_test)

print("--- 🎯 Model Performans Sonuçları ---\n")
print(f"Doğruluk Oranı (Accuracy): % {accuracy_score(y_test, y_pred) * 100:.2f}\n")
print("Detaylı Sınıflandırma Raporu:")
print(classification_report(y_test, y_pred))
