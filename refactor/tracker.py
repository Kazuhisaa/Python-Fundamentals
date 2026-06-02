import os 
import json
from dotenv import load_dotenv

class budgetTracker:
    def __init__(self):
        load_dotenv()
        self.__expenses = []
        self.__filename = os.getenv("DATABASE_FILE")
        self.load_expenses()

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