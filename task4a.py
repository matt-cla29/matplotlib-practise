import pandas as pd
import matplotlib as plt

df = pd.read_csv(r"C:\Users\734246\OneDrive - Bedford College\Documents\stuff\bookings.csv")
user_menu = int(input("enter a choice: "))
if user_menu == 1:
    for num in df:
        total += num
    print(df['Venue'])
elif user_menu == 2:
    for num in user_menu:
        total += num
    print(df['CustomerName'])
elif user_menu == 3:
    for num in user_menu:
        total += num
    print(df['DiscountPercent'])
elif user_menu == 4:
    for num in user_menu:
        total += num
    print(df['DiscountAmount'])
elif user_menu == 5:
    for num in user_menu:
        total += num
    print(df['Attendees'])
elif user_menu == 6:
    for num in user_menu:
        total += num
    print(df['HourlyRate'])
