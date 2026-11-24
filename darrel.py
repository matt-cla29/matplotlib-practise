total = 0
count = int(input("how many prices do you want?: "))

for i in range(count):
    priceloop = int(input(f"enter your price {i + 1}: "))
    total = total + priceloop
    print(f"total prices {count}, total is: {total: .2f}")


    