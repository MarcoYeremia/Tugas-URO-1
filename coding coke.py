Amount_Due = 50
while Amount_Due > 0:
    print("Amount Due:", Amount_Due)
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        Amount_Due -= coin
    else:
        continue

print("Change Owed:", abs(Amount_Due))

