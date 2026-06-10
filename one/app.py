import inventory

if __name__ == "__main__":
    
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
                view_stock()
            elif choice == 2:
                search_stock()
            elif choice == 3:
                add_stock()
            elif choice == 4:
                update_stock()
            elif choice == 5: 
                delete_stock()
            else:
                print("Please Refer to the number use in the Menu") 
        except ValueError:
            print("Please Refer to the number use in the Menu")
            
    
