import json
import os 


FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME,'r') as file:
            return json.load(file)
    return[]


def save_expenses(expenses):
    with open(FILENAME, 'w') as files:
        json.dump(expenses,files)


def add_expenses(expenses):

    entry = {
        "desc": input("What did you buy?"),
        "money": int(input("How Much is it?")),
        "date": input ("When did you bought it? ")
    }
    expenses.append(entry)
    save_expenses(expenses);


def view_expenses(expenses):
    for i,e  in enumerate(expenses):
        print(f"{i+1}. {e['desc']} | {e['money']} | {e['date']}")

def view_total_expenses(expenses):
    total_sum = 0;
    for i,e  in enumerate(expenses):
        total_sum += e['money']
    print ("-" * 20)
    print("Total Expenses: ", total_sum)


if __name__ == "__main__":
    expenses = load_expenses();

    while True:
        print("Expense Budget Tracker")
        print("1. Add Expenses")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Exit")
        choose = int(input("Choose: "))

        if choose == 1:
            add_expenses(expenses);
        elif choose == 2:
            view_expenses(expenses)
        elif choose == 3:
            view_total_expenses(expenses)
        elif choose == 4:
            break
        else:
            print("Invalid Input")
