import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

okut ="C:\\Users\\buğra\\Desktop\\index.csv"
data=pd.read_csv(okut)
print(data.head())

print(data.columns)
clen=data.dropna()
odeme=data["cash_type"]
adet=range(len(odeme))

plt.bar(odeme, adet)
plt.title('ödeme şekli')
plt.xlabel("Pay kind")
plt.ylabel("Value")
plt.show()