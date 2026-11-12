import json
import csv

# save expenses to a JSON file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
         json.dump(expenses, file)


# load expenses from a JSON file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []    
    # export expenses to a CSV file
def export_csv(expenses):
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
            writer.writerows(expenses)

