# كود تطبيق المحفظة الرقمية المتكامل
balance = 0.0 # رصيدك الحالي في المحفظة

while True:
    print("\n" + "="*30)
    print("      ALADDIN DIGITAL WALLET      ")
    print("="*30)
    print(f"Current Balance: {balance} USDT")
    print("-"*30)
    print("1. ➕ Deposit (إيداع)")
    print("2. ➖ Withdraw (سحب)")
    print("3. ❌ Exit (خروج)")
    print("-"*30)

    choice = input("Select an option (1-3): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print(f"✅ Success! Added {amount} USDT")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print(f"✅ Success! Withdrew {amount} USDT")
        else:
            print("❌ Error: Insufficient balance!")

    elif choice == "3":
        print("Closing Wallet... Goodbye!")
        break # هذا الأمر يغلق البرنامج

    else:
        print("❌ Invalid Choice! Try again.")
