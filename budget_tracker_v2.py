import os
import json

FILENAME = "expenses.json"
my_expenses = []

def save_expenses(my_expenses):
    with open(FILENAME, 'w') as f:
        json.dump(my_expenses,f)

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return json.load(f)
    return []

def add_expenses():
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
    my_expenses.append(expenses)
    save_expenses(my_expenses)

def view_expenses():
    for expenses in my_expenses:
        print(f"desc {expenses['desc']}, ₱ {expenses['price']}, date: {expenses['date']}")

def calculate_expenses():
    total_expenses = 0
    for expense in my_expenses:
        total_expenses += expense["price"]

    print("Total Expenses is : ", total_expenses)

my_expenses = load_expenses()

if __name__ == "__main__":
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
                add_expenses()
            elif choose == 2:
                view_expenses()
            elif choose == 3:
                calculate_expenses()   
            elif choose == 4:
                break
            else:
                print("Please Refer to the number use in the Menu")
        except ValueError:
            print("Please Refer to the number use in the Menu.")            
            

