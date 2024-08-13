menu={
    "Pizza":100,
    "Pasta":50,
    "Burger":50,
    "Salad":70,
    "Coffee":80
    
}
print("Welcome to our Resturant")

for item,price in menu.items():
    print(f"{item} : {price}")


total_price=0
def ordered_list(item,price):
    item=item.capitalize()
    print(item) 
    if item in menu:
       price=price+menu[item]
       print(f"{item} has been added in order list and total price is {price}")
    else:
       print(f"Ordered {item} is not available")   

item_1=input("Enter your first order : ")

ordered_list(item_1,total_price)

print("total",total_price)
more_order=input("Do you want to add another items Y for yes /N for No")
more_order=more_order.lower()
if(more_order == "y" or more_order == "yes"):
    item=input("Enter the second item")
    ordered_list(item,total_price)

# item_1=item_1.capitalize()
# print(item_1) 
# if item_1 in menu:
#     total_price=total_price+menu[item_1]
#     print(f"{item_1} has been added in order list and total price is {total_price}")
# else:
#     print(f"Ordered {item_1} is not available")   
    
    