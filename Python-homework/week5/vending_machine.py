amount_due = 50

while amount_due > 0:
    coin_input = input("Insert Coin: ")

    if not coin_input.isdigit() and not (coin_input.startswith("-") and coin_input[1:].isdigit()):
        print("Please insert a valid integer coin")
        continue

    coin = int(coin_input)

    if coin not in [5, 10, 25]:
        print(f"Coin not accepted. Returning {coin} cents")
        print(f"Amount Due: {amount_due}")
        continue

    amount_due -= coin

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

print(f"Change Owed: {abs(amount_due)}")

