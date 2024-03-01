import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

astronot=pd.read_csv("astronauts.csv")

#ilk 5 astronot bilgisi
print(astronot.head())

#Kategoriler
print(astronot.columns)

#Değerlerin ortalamasını 
print(astronot.describe())

#Boş değer olup olmadığının sorgusu
print(astronot.isnull())

#Boş satırları silme
astronot=astronot.dropna()
print(astronot)

#Bazı sütunları silme
df = astronot.drop('Birth Date', axis=1)
df = astronot.drop('Military Branch', axis=1)
df = astronot.drop('Death Mission', axis=1)
print(df)



#Cinsiyet dağılım grafiği
astronot["Gender"].value_counts().plot(kind='bar')
plt.title("cinsiyet Dağılımı")
plt.xlabel("Cinsiyet")
plt.ylabel("Kişi sayısı")
plt.show()

#Şimdiki durumları
astronot["Status"].value_counts().plot(kind='bar')
plt.title("Şimdiki Durumları")
plt.ylabel("Kişi sayısı")
plt.show()

#Uzayda yürüyüş yapmayan astronot sayısı
print(astronot["Space Walks"].value_counts())

#ilk 15 kişinin görevi
ilk_15_gorev = astronot.head(15)['Missions']
print(ilk_15_gorev)

#gittikleri okul
astronot["Alma Mater"].value_counts().plot(kind='bar')
plt.show()

#yıllara göre uzaya giden cinsiyet
astronot_sayilari = astronot.groupby(['Year', 'Gender']).size().unstack(fill_value=0)

astronot_sayilari.plot(kind='bar', stacked=True, color=['blue', 'pink'], figsize=(10, 6))
plt.title('Yıllara Göre Uzaya Giden Kadın ve Erkek Astronot Sayısı')
plt.xlabel('Yıl')
plt.ylabel('Astronot Sayısı')
plt.legend(title='Cinsiyet', labels=['Erkek', 'Kadın'])
plt.show()
