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
            choice = int(input("Please Choose A Number: "))

            if choice == 1:
                inv.view_stock()
            elif choice == 2:
                print("Please type the product you want to search: ")
                inv.search_product()
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
                
            elif choice == 4:
                choice = int(input("what do you want to update? "))
                print("1. Product Information")
                print("2 Replenish Product")

                if choice == 1:
                    inv.update_product_info
                elif choice == 2:
                    inv.replenish_stock
                else:
                    print("Please refer to the Menu")
            elif choice == 5: 
                inv.delete_stock()
            else:
                print("Please Refer to the number use in the Menu") 
        except ValueError:
            print("Please Refer to the number use in the Menu")
            
    
