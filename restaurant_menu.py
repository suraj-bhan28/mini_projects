menu={
    'Pasta':90,
    'Burger':40,
    'Pizza':199,
    'Meggi':80,
    'Cold Coffee':50,
    'Ice-Cream':70,
}
order_total=0
print("Welcome to the Bhavya Cafe")
print("****MENU****")
print("Pasta:Rs 90\n Burger:Rs 40\n Pizza:Rs 199\n Meggi:Rs 80\n Cold Coffee:Rs 50\n Ice-Cream:Rs 70\n")

item_1=input("Enter the item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} added to your order")

else:
    print(f"ordered item {item_1} is not available yet!")
    
second_order=input("Do you want to add more items? (Yes/No) ")
if second_order =="Yes":
    item_2=input("Enter the item you want to add =")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Your second item {item_2} is added in order")
    else:
        print(f"Your item {item_2} is not available yet!")
print(f"Total bill = {order_total}")