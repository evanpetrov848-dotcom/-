# --- إعدادات المنصة ---
exchange_rate = 550.0  # سعر الصرف (1 دولار = 550 جنيه)
commission_rate = 0.01  # عمولتك هي 1% من المبلغ

print("--- 📱 Welcome to Your USDT Exchange ---")
print(f"Current Rate: 1 USDT = {exchange_rate} SDG")
print(f"Our Commission: {commission_rate * 100}%")
print("---------------------------------------")

# 1. السؤال عن العملية
action = input("Type (buy) to purchase or (sell) to cash out: ").lower()

# 2. السؤال عن الكمية
amount = float(input("How many USDT? "))

# 3. حساب العمليات
if action == "buy":
    cost = amount * exchange_rate
    fee = cost * commission_rate
    total = cost + fee
    print(f"\n--- Receipt ---")
    print(f"Price: {cost} SDG")
    print(f"Fee (1%): {fee} SDG")
    print(f"TOTAL TO PAY: {total} SDG")

elif action == "sell":
    value = amount * exchange_rate
    fee = value * commission_rate
    total = value - fee
    print(f"\n--- Receipt ---")
    print(f"Price: {value} SDG")
    print(f"Fee (1%): {fee} SDG")
    print(f"YOU WILL RECEIVE: {total} SDG")

else:
    print("Invalid action! Please run the program again.")

print("---------------------------------------")
print("Thank you for using our service!")
