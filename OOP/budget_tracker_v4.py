import os 
import json

class budgetTracker:
    def __init__(self):
        self.__expenses = []
        self.__filename = "gastos.json"

    @property
    def expense_list(self):
        return self.__expenses
    
    def add_expenses(self):
        desc = input("What did you bought? ")
        date = input("when did you buy it? ")

        while True:
            try:
                price= int(input("How much is it? "))
                if price <= 0:
                    print("Please positive and real numbers. ")
                else: 
                    break 
            except ValueError:
                print("Please Use a Number")
        
        expense = {
            "desc": desc,
            "date": date, 
            "price": price
        }

        self.__expenses.append(expense)
        self.save_expenses()

    def save_expenses(self):
        with open(self.__filename, 'w') as f:
            json.dump(self.__expenses,f)

    def view_expenses(self):
        for expenses in self.__expenses:
            print(f" desc: {expenses['desc']}, Price: {expenses['price']}, Date:{expenses['date']}")

    def load_expenses(self):
        if os.path.exists(self.__filename):
            with open(self.__filename, 'r') as f:
                self.__expenses = json.load(f)
    
    def calculate_expense(self):
        total_expense = 0
        for expense in self.__expenses:
            total_expense += expense['price']
        
        print(total_expense)


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
            

    





