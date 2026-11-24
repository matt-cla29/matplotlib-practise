import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"bookings.csv")

x = (df["CustomerName"])
y = (df["HoursBooked"])
plt.bar(x, y, color="red")

plt.show()