import pandas as pd
import matplotlib.pyplot as plt

# Veri setini oku
df = pd.read_csv("StudentsPerformance.csv")

# Cinsiyete göre ortalama matematik puanı
ortalama_math = df.groupby('gender')['math score'].mean()

# Bar grafiği
ortalama_math.plot(kind='bar', color=['pink', 'lightblue'])
plt.title("Cinsiyete Göre Ortalama Matematik Puanı")
plt.ylabel("Ortalama Puan")
plt.xlabel("Cinsiyet")
plt.show()

# 2️⃣ Matematik Puanı Dağılımı (Histogram)
plt.figure(figsize=(6,4))
plt.hist(df['math score'], bins=10, color='lightgreen', edgecolor='black')
plt.title("Matematik Puan Dağılımı")
plt.xlabel("Matematik Puanı")
plt.ylabel("Öğrenci Sayısı")
plt.show()
