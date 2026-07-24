print("Currency Converter")
print("1. THB to USD")
print("2. USD to THB")
choice = input("Select the option you want(1 or 2): ")
#THB to USD
if choice == "1":
     thb_amount = float(input("Enter the amount(THB) : "))
     usd_amount = thb_amount / 35.5 
     print(f"your amount to USD : {usd_amount:.2f} $")

#USD to THB
elif choice == "2":
     usd_amount = float(input("Enter the amount(USD) : "))
     thb_amount = usd_amount * 35.5 
     print(f"your amount to THB : {thb_amount:.2f} ฿")
