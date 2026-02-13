
import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Failas užkrautas sėkmingai!")
print(df.head())

print("\nBendra pardavimų suma:")
print(df["sales"].sum())

print("\nVidutiniai pardavimai:")
print(df["sales"].mean())

print("\nPardavimai pagal regioną:")
print(df.groupby("region")["sales"].sum())

print("\nPardavimai pagal produktą:")
print(df.groupby("product")["sales"].sum())

import matplotlib.pyplot as plt

# Pardavimai pagal regioną
sales_by_region = df.groupby("region")["sales"].sum()

# Braižome grafiką
sales_by_region.plot(kind="bar")

plt.title("Pardavimai pagal regioną")
plt.xlabel("Regionas")
plt.ylabel("Pardavimai")
plt.xticks(rotation=0)

plt.savefig("outputs/sales_by_region.png")

plt.show()

# Pardavimai pagal produktą
sales_by_product = df.groupby("product")["sales"].sum()

sales_by_product.plot(kind="bar")

plt.title("Pardavimai pagal produktą")
plt.xlabel("Produktas")
plt.ylabel("Pardavimai")
plt.xticks(rotation=0)

plt.savefig("outputs/sales_by_product.png")

plt.show()





