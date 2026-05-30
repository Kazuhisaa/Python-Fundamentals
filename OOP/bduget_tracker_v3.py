import os
import json

class budget_tracker:
    def __init__(self):
        self.expense = []
        self.filename = "gastos.json"
        self.load_expenses()


    def add_expenses(self):
        desc = input("what did you buy? ")
        date = input("Date you bought it?")

        while True:
            try:
                price = int(input("How much it cost? "))
                if price <= 0: 
                    print("Don't use negative values")
                else:
                    break
            except ValueError:
                print("please use numbers")

        expenses = {
            "desc": desc,
            "price": price,
            "date": date
        }
            
        self.expense.append(expenses)
        self.save_expenses()

    def save_expenses(self):
        with open(self.filename,'w')as f:
            json.dump(self.expense,f)

    def view_expenses(self):
       for expenses in self.expense:
           print (f"desc:{expenses['desc']}, ₱: {expenses['price']}, Date: {expenses['date']} ")
    
    def calculate_expenses(self):
        total_expenses = 0
        for expenses in self.expense:
            total_expenses += expenses['price']
        print("Total Expenses: ", total_expenses)

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.expense = json.load(f)

if __name__ == "__main__":

    tracker = budget_tracker()

    while True:
        try:
            print("=================")
            print("BUDGET TRACKER V2")
            print("=================")
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
            

    





