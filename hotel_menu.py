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
    return price

def more_ordered(current_price):
   while True:
     more_order=input("Do you want to add another items Y for yes or N for No ")
     more_order=more_order.lower()
     if more_order in ["yes","y"]:
      item=input("Enter the next item ")
    
      current_price= ordered_list(item,current_price)
      print("current",current_price)
     elif more_order in ["no","n"]:
    #   print("current",current_price)
      return current_price
     else:
       print("Enter yes or not ")
       
    
item_1=input("Enter your first order ")
total_price=ordered_list(item_1,total_price)
total_price = more_ordered(total_price)
print("Thank you")
print(f"The total price for all your orders is: {total_price}")