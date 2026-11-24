import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


#The menu() function generates the UI the accepts and validates user choice
def menu():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Australian Dollars (AUD)")
        print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("7. American Dollar (USD) to Pound Sterling (GBP)")
        print("8. Pound Sterling (GBP) to American Dollar (USD)")
        print("9.  the value of the pound (GBP) compared to other currencies")
        print("10. the performance (e.g. increase/decrease in value) of a selected currency")
        print("######################################################")

        
        menu_choice = int(input("Please enter the number of your choice (1-10): "))

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 10:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return menu_choice  


#Gets the short version of the conversion information based on user menu choice
def get_currency ():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GBP - JPY',
        '6': 'JPY - GBP',
        '7': 'USD - GBP',
        '8': 'GBP - USD'}
   
    currency = currencies.get((str(menu_choice)))
    
    return currency


def pounds_to_other_currencies():
    if menu_choice == 9 :
        print("thank for you for choosing to see the value of the pound compared to other currencies")
        currency_choice = int(input("which currency would you like to see the value of the pound compared to? \n 1. Euros (EUR) 2. Australian Dollars (AUD) 3. Japanese Yen (JPY) 4, American Dollar (USD): "))
        if currency_choice == 1:
            df = pd.read_csv("Task4a_RBSX_data.csv")
            df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, format="mixed")
            x = (df["Date"])
            y = (df["GBP - EUR"])
            plt.plot(x, y, color="red")
            plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=10))
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
            plt.title("Value of GBP against EUR")
            plt.xlabel("Date")
            plt.ylabel("Euros per pound")
            plt.xticks(rotation=45)
            plt.tight_layout()  
            plt.show()   
        elif currency_choice == 2:
            df = pd.read_csv("Task4a_RBSX_data.csv")
            df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, format="mixed")
            x = (df["Date"])
            y = (df["GBP - AUD"])
            plt.plot(x, y, color="red")
            plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=10))
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
            plt.title("Value of GBP against AUD")
            plt.xlabel("Date")
            plt.ylabel("Australian Dollar per pound")
            plt.xticks(rotation=45)
            plt.tight_layout()  
            plt.show()
        elif currency_choice == 3:
            df = pd.read_csv("Task4a_RBSX_data.csv")
            df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, format="mixed")
            x = (df["Date"])
            y = (df["GBP - JPY"])
            plt.plot(x, y, color="red")
            plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=10))
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
            plt.title("Value of GBP against JPY")
            plt.xlabel("Date")
            plt.ylabel("Japanese Yen per pound")
            plt.xticks(rotation=45)
            plt.tight_layout()  
            plt.show() 
        elif currency_choice == 4:
            df = pd.read_csv("Task4a_RBSX_data.csv")
            df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, format="mixed")
            x = (df["Date"])
            y = (df["GBP - USD"])
            plt.plot(x, y, color="red")
            plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=10))
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
            plt.title("Value of GBP against USD")
            plt.xlabel("Date")
            plt.ylabel("American Dollar per pound")
            plt.xticks(rotation=45)
            plt.tight_layout()  
            plt.show() 


def performance_of_currency():

    print("Which currency performance would you like to see?")
    print("1. Euros (EUR)")
    print("2. Australian Dollars (AUD)")
    print("3. Japanese Yen (JPY)")
    print("4. Pound Sterling (GBP)")
    print("5. American Dollars (USD)")

    perform_choice = int(input("Enter your choice: "))

    currencies = {
        1: "EUR",
        2: "AUD",
        3: "JPY",
        4: "GBP",
        5: "USD"
    }

    if perform_choice not in currencies:
        print("Invalid choice")
        return

    selected_currency = currencies[perform_choice]

    df = pd.read_csv("Task4a_RBSX_data.csv")

    df["Date"] = pd.to_datetime(
        df["Date"], dayfirst=True, format="mixed"
    )

    # Store the exchange rates
    rates = pd.DataFrame({
        "GBP": 1,
        "EUR": df["GBP - EUR"],
        "AUD": df["GBP - AUD"],
        "JPY": df["GBP - JPY"],
        "USD": df["GBP - USD"]
    })

    # Select the other four currencies
    other_currencies = [
        currency for currency in rates.columns
        if currency != selected_currency
    ]

    # Create four graphs
    figure, axes = plt.subplots(2, 2, figsize=(12, 8))

    for ax, currency in zip(axes.flat, other_currencies):

        y = rates[currency] / rates[selected_currency]

        ax.plot(df["Date"], y)

        ax.set_title(selected_currency + " against " + currency)
        ax.set_xlabel("Date")
        ax.set_ylabel(currency + " per " + selected_currency)

        ax.grid()

    figure.suptitle("Performance of " + selected_currency)

    figure.autofmt_xdate()
    figure.tight_layout()

    plt.show()



#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_RBSX_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate


#Accepts and validates user input for the amount they want to convert
def get_amount_to_convert():
    print("You are converting: ",currency)
    
    flag = True

    while flag:
        conversion_amount = input("please enter the amount you wish to convert: ")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  


#Performs the conversion and outputs the final values
def perfom_conversion():
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will receive {} in {}'.format(amount_recieved, currency[6:9]))

menu_choice = menu()

if menu_choice <= 8:
    currency = get_currency()

    conversion_rate = get_conversion_rate()

    
    conversion_amount = float(get_amount_to_convert())

    perfom_conversion()

elif menu_choice == 9:
    pounds_to_other_currencies()

elif menu_choice == 10:
    performance_of_currency()
   
