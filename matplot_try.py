import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\734246\OneDrive - Bedford College\Documents\stuff\bookings.csv")

x = (df["CustomerName"])
y = (df["HoursBooked"])
plt.bar(x, y, barcolor="red")

plt.show()