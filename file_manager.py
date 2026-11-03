import json

# save expenses to a JSON file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
