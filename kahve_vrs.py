import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

okut ="C:\\Users\\buğra\\Desktop\\index.csv"
data=pd.read_csv(okut)
print(data.head())

print(data.columns)
clen=data.dropna()
odeme=data["cash_type"]
cafe_name=data["coffee_name"]
cafe_price=data["money"] 
credit_cart=data['card']
adet=range(len(odeme))

""" pay types """
plt.bar(odeme, adet)
plt.xlabel("Pay kind")
plt.ylabel("Value")
plt.title("pay - types")
plt.grid(True, alpha=0.2)
plt.show()


""" cafe name , price grafik """
plt.bar(cafe_name ,cafe_price)
plt.xlabel("name")
plt.ylabel("price")
plt.title("cafe- name, price")
plt.grid(True, alpha=0.2)
plt.show()

sns.set_style("whitegrid")
sns.scatterplot(x=cafe_name , y=cafe_price , hue=odeme , size=cafe_price , style=odeme ,data=data)
plt.xlabel("name")
plt.ylabel("price")
plt.show()


