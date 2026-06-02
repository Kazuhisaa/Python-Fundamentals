from tracker import budgetTracker
if __name__ == "__main__":

    tracker = budgetTracker()

    while True:
        try:
            print("=================")
            print("BUDGET TRACKER V3")
            print("=================")
            print(f"Total Transacations: {len(tracker.expense_list)}")
            print("1. Add Expesnes")
            print("2. View Expenses")
            print("3. Calculate Expenses")
            print("4. Exit")
            choose = int(input("Please Choose the number you want to do."))

            if choose == 1:
                tracker.add_expenses()
            elif choose == 2:
                tracker.view_expenses()
            elif choose == 3:
                tracker.calculate_expenses()   
            elif choose == 4:
                break
            else:
                print("Please Refer to the number use in the Menu")
        except ValueError:
            print("Please Refer to the number use in the Menu.")            
            

    
