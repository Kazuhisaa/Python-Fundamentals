import inventory

if __name__ == "__main__":
    inv = inventory.Inventory()
    
    while True: 
        try:
            print("====================")
            print("= Inventory System =")
            print("====================")
            print ("1. View Stock")
            print("2. Search Stock")
            print("3. Add stock")
            print("4. Update Stock")
            print("5. Delete Stock")
            print("6. Exit")
            choice = int(input("Please Choose A Number: "))

            if choice == 1:
                inv.view_stock()
            elif choice == 2:
                query = input("Please input product id or the name to search. ")
                found_product = inv.search_product(query)
                if found_product == None:
                    print("No product is found")
                else:
                    print(found_product.get_details())                
            elif choice == 3:
                print("What product you want to add? ")
                print("1. Clothing")
                print("2. Electronics")
                print("3. Food")
                choose = int(input("what Number do you want? "))
                
                if choose == 1:
                    product_id = input("Enter Product ID: ")
                    price = float(input("Enter Price: "))
                    name = input("Enter Product Name: ")
                    stocks = int(input("Enter Stocks: "))
                    size = input("Enter Size (S/M/L): ")
                    material = input("Enter Material: ")

                    new_item = inventory.Clothing(product_id, price, name, stocks, size, material)
                    inv.add_stock(new_item)

                elif choose == 2:
                    product_id = input("Enter Product ID: ")
                    price = float(input("Enter Price: "))
                    name = input("Enter Product Name: ")
                    stocks = int(input("Enter Stocks: "))
                    warranty = input("Enter Warranty: ")

                    new_item = inventory.Electronics(product_id, price, name, stocks,warranty)
                    inv.add_stock(new_item)

                elif choose == 3:
                    product_id = input("Enter Product ID: ")
                    price = float(input("Enter Price: "))
                    name = input("Enter Product Name: ")
                    stocks = int(input("Enter Stocks: "))
                    expiration = input("Enter Expiration")
                    is_vegan = (input("It is Vegan? (y/n):  ").strip().lower() == 'y')

                    new_item = inventory.Food(product_id, price, name, stocks,expiration,is_vegan)
                    inv.add_stock(new_item)
                else:
                    print("Please Refer to the menu")

            elif choice == 4:
                print("1. Product Information")
                print("2 Replenish Product")
                want = int(input("what do you want to update? "))
                if want == 1:
                    product_id = input("Enter Product id: ")
                    new_name = input("Enter New Name: ")
                    new_price = float(input("Enter New Price"))
                    inv.update_product_info(product_id, new_name, new_price)
                elif want == 2:
                    product_id = input("Enter Product id: ")
                    qty = int(input("Enter Quantity: "))
                    if qty <= 0:
                        print("Please use positive numbers.")
                    else:
                        inv.replenish_stock(product_id, qty)
                else:
                    print("Please refer to the Menu")

            elif choice == 5: 
                product_id = input("Enter Product ID: ")
                inv.delete_product(product_id)
            elif choice == 6:
                break
            else:
                print("Please Refer to the number use in the Menu") 
        except ValueError:
            print("Please Refer to the number use in the Menu")
            
    
