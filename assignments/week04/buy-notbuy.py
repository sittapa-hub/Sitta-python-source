items_list = []
bought_list = []
spent = 0
print("Enter prices of 6 items:")

for i in range(6):
    item = int(input(f"Item {i+1}: "))
    items_list.append(item)

budget = int(input("\nEnter total budget: "))


for j in range(len(items_list)):
    if budget >= items_list[j]:
        bought_list.append(items_list[j])
        spent += items_list[j]
        budget -= items_list[j]
        print(f"\nItem {j+1} = {items_list[j]} -> buy")
        print("Current total = ",spent)
    else:
        print(f"\nItem {j+1} = {items_list[j]} -> cannot buy")
        print("Current total = ",spent)

print("\nBought items: ",bought_list)
print("Total spent: ",spent)
print("Remaining budget: ",budget)