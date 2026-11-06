import json

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

